import re
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .utils.embedding import get_embedding
from .utils.es_client import es

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def extract_price_filter(query):
    match = re.search(r'under\s+(\d+)', query, re.IGNORECASE)
    return int(match.group(1)) if match else None

@api_view(['POST'])
def search_view(request):
    query = request.data.get("query", "")
    if not query:
        return Response({"error": "Missing query"}, status=400)

    query_vector = get_embedding(query)
    max_price = extract_price_filter(query)

    es_query = {
        "size": 5,
        "query": {
            "script_score": {
                "query": {
                    "bool": {
                        "should": [
                            {"match": {"name": {"query": query, "boost": 2}}},
                            {"match": {"description": query}}
                        ],
                        **({"filter": [{"range": {"price": {"lte": max_price}}}]} if max_price else {})
                    }
                },
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": query_vector}
                }
            }
        }
    }

    res = es.search(index="products", body=es_query)
    results = [hit["_source"] for hit in res["hits"]["hits"]]
    return Response({"results": results})
