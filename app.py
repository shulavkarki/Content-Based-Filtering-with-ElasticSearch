from fastapi import FastAPI
from sentence_transformers import SentenceTransformer

import config
from connectelastic import connect_elastic
from model import Query, ResOut
# Importing the StemTokenizer class from the preprocessing.py file.
from preprocessing import StemTokenizer
from search_es import search_topN

model = SentenceTransformer(config.MODEL_NAME)
preprocess = StemTokenizer()
es = connect_elastic(config.ENDPOINT, config.ELASTIC_USER, config.ELASTIC_PASSWORD)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/recommend/", response_model=dict[int, ResOut])
def get_recommendations(query: Query):
    """
    It takes in a movie name and number of recommendations as input, preprocesses the movie name,
    encodes it using the sbert(a sentence encoder), and then searches for the top N recommendations
    using Elasticsearch

    :param query: This is the input parameter that we will pass to the API. It is a class that contains
    the movie name and the number of recommendations we want
    :return: A list of movie names
    """
    # dicti = collections.defaultdict(list)
    dicti = {}
    processed_query = preprocess(query.movie_name)
    # print(query.movie_name)
    query_vec = model.encode(processed_query).tolist()
    # print(query_vec)
    response = search_topN(query_vec, es, query.no_of_recommendation)
    print("Searching the for the top recommendations...")

    for res in response:
        dicti[res["_id"]] = ResOut(**res["_source"])
    return dicti


# @app.post("/search/", response_model = dict[int, ResOut])
# def search(query:Query):
#     """
#     It takes a query object as input, searches for the movie name in the elasticsearch index and returns
#     the top n similar contents

#     :param query: Query
#     :type query: Query
#     :return: A list of movie names
#     """
#     response = search_movies(query.movie_name, es, query.no_of_recommendation)
#     dicti = {}
#     for res in response:
#         dicti[res["_id"]] = ResOut(**res["_source"])
#     return dicti
