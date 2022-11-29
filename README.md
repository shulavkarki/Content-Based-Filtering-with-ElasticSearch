# Content-Based-Filtering-with-ElasticSearch
A Movie recommendation system using Content Based Filtering with ElasticSearch
## Built With
- Python
- ElasticSearch
- Sbert
- FastApi
- NLTK
- Pandas

## Getting Started

### Installation
1. Clone the repo
```
git clone https://github.com/shulavkarki/Content-Based-Filtering-with-ElasticSearch.git
```
2. Create Virtual Env.
```
python -m venv {environmentname}
```
3. Install the requirements.
```
pip install -r requirements.txt
```
4. Fire up the elasticsearch and kibana service with docker.
```
docker-compose up
```
> run docker desktop.
> Make sure the elasticsearch and kibana is working by going to following ports.
```localhost:9200```
```localhost:5601```  
> You should get something like this:  
![image](https://user-images.githubusercontent.com/40908371/204493348-2d122b0c-cfe7-449c-93fc-512869abe2f4.png)  
![image](https://user-images.githubusercontent.com/40908371/204493447-f1e47659-26b2-4551-a20c-60fe246dd229.png)

5. Index the movie.
> For indexing movies to elasticsearch. Run the following.
```
python create_index.py
```

6. Run Fastapi
```
uvicorn foldername.app:app --reload
```
