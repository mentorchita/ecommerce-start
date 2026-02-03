import json
import random
from faker import Faker
import pandas as pd

# Ініціалізуємо Faker для генерації фейкових даних
fake = Faker()

# Визначимо категорії товарів для e-commerce
categories = [
    'Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Sports & Outdoors',
    'Beauty & Personal Care', 'Toys & Games', 'Grocery', 'Automotive', 'Health'
]

# Функція для генерації даних про продукти
def generate_products(num_products=100):
    products = []
    for i in range(1, num_products + 1):
        product = {
            'product_id': i,
            'name': fake.word().capitalize() + ' ' + random.choice(['Pro', 'Max', 'Ultra', 'Lite', 'Essential']),
            'category': random.choice(categories),
            'price': round(random.uniform(5.0, 500.0), 2),
            'description': fake.sentence(nb_words=10),
            'stock': random.randint(0, 100)
        }
        products.append(product)
    return products

# Функція для генерації відгуків (reviews) для продуктів
def generate_reviews(products, num_reviews_per_product=5):
    reviews = []
    for product in products:
        for _ in range(num_reviews_per_product):
            review = {
                'product_id': product['product_id'],
                'user_id': random.randint(1, 50),  # Припустимо 50 користувачів
                'rating': random.randint(1, 5),
                'review_text': fake.paragraph(nb_sentences=2),
                'date': fake.date_time_this_year().isoformat()
            }
            reviews.append(review)
    return reviews

# Функція для генерації користувацьких запитів (queries) для агента
def generate_user_queries(num_queries=50):
    query_templates = [
        "Recommend {category} under {price}$",
        "What are the best {category} products?",
        "Show reviews for {product_name}",
        "Find {category} with rating above {rating}",
        "Suggest alternatives to {product_name}",
        "What's the price of {product_name}?",
        "Help me choose a {category} for {purpose}"
    ]
    purposes = ['daily use', 'gifts', 'work', 'travel', 'sports']
    queries = []
    for _ in range(num_queries):
        template = random.choice(query_templates)
        query = template.format(
            category=random.choice(categories),
            price=random.randint(50, 300),
            product_name=fake.word().capitalize() + ' Item',
            rating=random.randint(3, 5),
            purpose=random.choice(purposes)
        )
        queries.append({'query_id': len(queries) + 1, 'query_text': query})
    return queries

# Функція для генерації взаємодій користувачів (interactions: ratings, purchases)
def generate_interactions(num_users=50, num_interactions=200):
    interactions = []
    for _ in range(num_interactions):
        interaction = {
            'user_id': random.randint(1, num_users),
            'product_id': random.randint(1, 100),  # Припустимо 100 продуктів
            'action': random.choice(['view', 'add_to_cart', 'purchase', 'rate']),
            'timestamp': fake.date_time_this_month().isoformat(),
            'rating': random.randint(1, 5) if random.choice([True, False]) else None
        }
        interactions.append(interaction)
    return interactions

# Головна функція для генерації всіх даних та збереження
def generate_ecommerce_data(output_dir='ecommerce_data'):
    products = generate_products(100)
    reviews = generate_reviews(products, 5)
    queries = generate_user_queries(50)
    interactions = generate_interactions(50, 200)

    # Збереження в JSON
    with open(f'{output_dir}/products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    
    with open(f'{output_dir}/reviews.json', 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=4)
    
    with open(f'{output_dir}/user_queries.json', 'w', encoding='utf-8') as f:
        json.dump(queries, f, ensure_ascii=False, indent=4)
    
    # Збереження взаємодій в CSV за допомогою pandas
    df_interactions = pd.DataFrame(interactions)
    df_interactions.to_csv(f'{output_dir}/interactions.csv', index=False)

    print(f"Дані згенеровано та збережено в директорії '{output_dir}'")

# Виклик функції
if __name__ == "__main__":
    generate_ecommerce_data()
