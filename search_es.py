import config

def search_topN(query_vec, es, no_of_recommendation):
    """
    It takes a vector as input and returns the top 10 movies that are most similar to the input vector.
    
    :param query_vec: The vector of the query movie
    """
    
    script_query = {
        "script_score" : {
            "query" : {
                "match_all" : {}
            },
            "script" : {
                "params": {"query_vector": query_vec},
                "source" : "cosineSimilarity(params.query_vector, 'embedding') + 1.0"
            }
            
        }
    }   
    response = es.search(
        index = config.INDEX_NAME,
        body = {
            "size" : no_of_recommendation,
            "query": script_query,
            "_source": ["movie_name", 'genre']
        }
    )
    return response['hits']['hits']

def search_movies(query, es, no_of_content):
    """
    It takes a query string, connects to the Elasticsearch cluster, and returns the top 10 results
    
    :param query: The query string to search for
    """

    script_query = {
            "query" : {
                "match" : {
                    'movie_name': query
                },
            },
        },
    response = es.search(
        index = config.INDEX_NAME,
        body = script_query,
        size = no_of_content,
    )

    return response['hits']['hits']