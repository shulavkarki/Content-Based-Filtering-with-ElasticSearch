import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from connectelastic import connect_elastic
from index_map import insert_df_row
from preprocessing import StemTokenizer
import config

def process_df(path:str, preprocess:StemTokenizer, model:SentenceTransformer, es):
    """
    It takes a path to a csv file, a preprocessing function, and a sentence transformer model. It then
    iterates through the csv file, and for each row, it creates a document with the movie name, genre,
    embedding, and movie id. It then inserts the document into the database
    
    :param path: The path to the csv file containing the movie data
    :param preprocess: This is the preprocessing function 
    :param model: The sentence transformer model(sbert) to encode the text
    """
    df = pd.read_csv(path, sep=",")
    for id, row in df.iterrows():
        doc = {
            'movie_name':row['title'],
            'genre':row['genres'],
            'embedding': model.encode(preprocess(row['features'])).tolist(),
            'movie_id':id,
        }
        insert_df_row(doc, es)
        print(f"MovieId{id} indexed Sucessfully.") 

    
if __name__ == "__main__":
    preprocess = StemTokenizer()
    model = SentenceTransformer(config.MODEL_NAME)
    es = connect_elastic(config.ENDPOINT, config.ELASTIC_PASSWORD)
    process_df(config.DATA_PATH, preprocess, model, es)