from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from .utils.embedding import get_embedding
from .utils.es_client import es, create_index

@receiver(post_save, sender=Product)
def index_product(sender, instance, **kwargs):
    create_index()
    embedding = get_embedding(instance.description)
    doc = {
        "name": instance.name,
        "description": instance.description,
        "category": instance.category,
        "price": instance.price,
        "embedding": embedding
    }
    es.index(index="products", id=instance.id, body=doc)
