from django.contrib import admin
from .models import Product  # or from blog.models import Post if needed

admin.site.register(Product)
