# BestBuy App
The **BestBuy app** is a Python-based application that uses an object-oriented approach to manage products and facilitate purchases. This app includes functionalities for adding and removing products, checking product availability, and processing orders efficiently.
It has a **Product** class that represents each product with attributes such as name, price, quantity and active status, as well as methods to manage these attributes. 
The **Store** class contains a list of products and includes methods for adding and removing products, retrieving the total quantity of items, retrieving all active products and processing orders based on a shopping list of product-quantity pairs.

## Features
- **Product Management**: Represent each product with attributes like name, price, quantity, and active status.
- **Store Management**: Handle a list of products and perform various operations such as adding, removing, and listing products.
- **Order Processing**: Process orders based on a shopping list of product-quantity pairs, updating product quantities accordingly.

## Installation
- Clone the repository:
```
git clone https://github.com/mariacristinafadgyas/BestBuy
```
- Navigate to the project directory:
```
cd BestBuy
```
- Run the application:
```
python main.py
```

## Testing
To test the code, follow these steps:

1. Install the testing framework:
```
pip install pytest
```
2. Run the tests by executing the following command in the terminal:
```
pytest test_product.py
```
