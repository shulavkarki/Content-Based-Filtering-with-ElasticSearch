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

5. Index the movie.
> For indexing movies to elasticsearch. Run the following.
```
python create_index.py
```

6. Run Fastapi
```
uvicorn foldername.app:app --reload
```
