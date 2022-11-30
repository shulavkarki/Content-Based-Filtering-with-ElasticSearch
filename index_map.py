from config import settings


def create_df_index(es):
    """
    If the index doesn't exist, create it.
    """
    index_body = {
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 1,
        },
        "mappings": {
            "properties": {
                "movie_name": {
                    "type": "text",
                },
                "embedding": {"type": "dense_vector", "dims": 384},
                "genre": {
                    "type": "text",
                },
                "movie_id": {"type": "text"},
            }
        },
    }
    try:

        # Ignore 400 means to ignore "Index Already Exist" error.
        es.indices.create(index=settings.INDEX_NAME, body=index_body)  # ignore=[400, 404]
        print(f"Created Index -> {settings.INDEX_NAME}")
        # else:
        # print(f"Index {settings.INDEX_NAME} exists...")
    except Exception as ex:
        print(str(ex))


def insert_df_row(doc, es):
    """
    It checks if the index exists, if not, it creates it, then it indexes the document.

    :param doc: The document to be inserted
    """
    if not es.indices.exists(settings.INDEX_NAME):
        create_df_index(es)
    # try:
    es.index(index=settings.INDEX_NAME, body=doc)
