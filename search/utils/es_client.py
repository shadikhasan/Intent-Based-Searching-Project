from elasticsearch import Elasticsearch
import os

ES_HOST = os.getenv("ES_HOST", "http://elasticsearch:9200")
es = Elasticsearch(ES_HOST)

def create_index():
    if not es.indices.exists(index="products"):
        es.indices.create(index="products", body={
            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "description": {"type": "text"},
                    "category": {"type": "text"},
                    "price": {"type": "float"},
                    "embedding": {"type": "dense_vector", "dims": 384}
                }
            }
        })
