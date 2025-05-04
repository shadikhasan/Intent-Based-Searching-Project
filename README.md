# 🛍️ Semantic Product Search with Django & Elasticsearch (AI Hackathon Project)

This project was developed as part of the [Poridhi.io AI Hackathon](https://poridhi.io/hackathon). It focuses on creating a semantic product search engine using **NLP embeddings**, **Elasticsearch**, and **Django REST Framework** to help users find products based on their intent and natural language queries.

## 🚀 Hackathon Overview

- **Event:** AI Hackathon by Poridhi.io
- **Theme:** Building intelligent search systems using AI technologies
- **Duration:** 12 hours
- **Team Name:** RU_tob_tobi_tob

## 🎯 Project Goal

The goal of this project is to build a semantic search engine that allows users to search for products with natural language queries. Instead of relying solely on keyword matching, this system uses **Sentence Transformers** to generate embeddings and rank product descriptions based on their semantic similarity to the query.

### Features

- 🔍 **Intent-Based Search** using sentence embeddings
- 🧠 **Semantic Matching** using cosine similarity
- 🗃️ **Product Indexing** with category, description, and price
- 📦 **Elasticsearch Integration** for fast, intelligent querying
- 🧰 **REST API** powered by Django REST Framework
- 🐳 **Docker-Ready** for easy deployment

## 📦 Tech Stack

- **Backend:** Django, Django REST Framework
- **Search Engine:** Elasticsearch
- **NLP:** Sentence Transformers (`all-MiniLM-L6-v2`)
- **Containerization:** Docker, Docker Compose

## 🧠 How It Works

1. A product is saved via the Django admin or API.
2. A signal computes the sentence embedding of the product description using Sentence Transformers.
3. The product is indexed in Elasticsearch with both metadata and its embedding vector.
4. When a user submits a search query:
   - The query is vectorized using the same model.
   - Elasticsearch searches for products by combining traditional text matching and cosine similarity on vectors.
   - Optional filter: `"under $X"` queries extract price limits via regex.

## 🔧 Project Structure

```
.
├── intent_search/
│   ├── models.py          # Product model
│   ├── serializers.py     # DRF serializer
│   ├── views.py           # Search + product CRUD views
│   ├── urls.py            # API routes
│   ├── signals.py         # Auto index to Elasticsearch
│   └── utils/
│       ├── embedding.py   # SentenceTransformer embedding function
│       └── es_client.py   # Elasticsearch client and index creation
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🧪 Sample Query Handling

**Query:** `smartphone under 500`

- Extracts "smartphone" as the semantic intent.
- Uses regex to detect price filter (`under 500`).
- Embeds the query with Sentence Transformers.
- Combines:
  - `match` on `name` and `description`
  - cosine similarity on embedding vector
  - optional `price` filter

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose installed

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shadikhasan/Intent-Based-Searching-Project.git
   cd Intent-Based-Searching-Project
   ```

2. **Start the App**

   ```bash
   docker-compose up --build
   ```

   This will:

   - Build and run Django
   - Pull and run Elasticsearch
   - Run Migrations

3. **Run Migrations**

   In a new terminal:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create Superuser (optional)**

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## 🎯 API Endpoints

| Method | Endpoint     | Description                     |
| ------ | ------------ | ------------------------------- |
| GET    | `/products/` | List all products               |
| POST   | `/products/` | Add a new product               |
| POST   | `/search/`   | Semantic search with query JSON |

## 🔎 Sample Search Request

**POST** `/search/`

```json
{
  "query": "wireless headphones under 100"
}
```

**Response**

```json
{
  "results": [
    {
      "name": "Sony Wireless Headphones",
      "description": "Noise cancelling headphones with long battery life.",
      "category": "Audio",
      "price": 89.99
    }
  ]
}
```

## 🧠 Improvements (To-Do)

- Integrate frontend for user interaction
- Add support for multi-lingual embeddings
- Pagination support in search
- Unit tests for API and search logic

## 📜 License

This project is licensed under the MIT License.

