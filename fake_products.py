from faker import Faker
import random

fake = Faker()

def generate_fake_product():
    product_name = fake.word() + ' ' + fake.word()
    category = fake.word()
    description = fake.text()
    price = round(random.uniform(1, 1000), 2)  # Random price between 1 and 1000
    stock_quantity = random.randint(1, 1000)

    product_data = {
        'product_name': product_name,
        'category': category,
        'description': description,
        'price': price,
        'stock_quantity': stock_quantity,
    }

    return product_data

def generate_fake_products(num_products):
    products = []
    for _ in range(num_products):
        product = generate_fake_product()
        products.append(product)
    return products

if __name__ == "__main__":
    num_products_to_generate = 10  # Change this to the desired number of fake products

    fake_products = generate_fake_products(num_products_to_generate)

    for idx, product in enumerate(fake_products, start=1):
        print(f"Product {idx}:")
        print(f"  Name: {product['product_name']}")
        print(f"  Category: {product['category']}")
        print(f"  Description: {product['description']}")
        print(f"  Price: ${product['price']}")
        print(f"  Stock Quantity: {product['stock_quantity']}")
        print("\n")
