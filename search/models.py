from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Electronics", "Electronics"),
        ("Audio", "Audio"),
        ("Gaming", "Gaming"),
        ("Fitness", "Fitness"),
        ("Fashion", "Fashion"),
        ("Furniture", "Furniture"),
        ("Kitchen", "Kitchen"),
        ("Books", "Books"),
        ("Accessories", "Accessories"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.FloatField()

    def __str__(self):
        return self.name
