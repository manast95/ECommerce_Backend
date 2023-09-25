# Problem Statement:

 __To create a sample E-commerce backend application like Flipkart/Amazon.__
 __Tech Stack used: Python - FastAPI with MongoDB as a database using pymongo.__

# Recommended IDE to run this Project:
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows)
- [Visual Studio Code](https://code.visualstudio.com/download)

# Steps required to run this Project:
### Setup and activate a Python virual environment (can be automatically done using PyCharm):
```
virtualenv venv
```
For Linux/Mac
```
source venv/bin/activate
```
For Windows
```
source venv/Scripts/activate
```
### Install the following packages using PIP:
```
pip install fastapi pymongo uvicorn
```
### Start the server:
```
uvicorn main:app --reload 
```

### Use the Swagger UI:
```
http://127.0.0.1:8000/docs 
```

### Code Structure:
```
config/db.py

This code establishes a connection to MongoDB using the PyMongo library. It connects to a local MongoDB instance by default, but you can also use it with MongoDB Atlas by providing the appropriate connection URI with a username and password.
```
```
models/user.py

This code defines several Pydantic models for representing different data entities.

User Model
name: A string representing the user's name.
price: A float representing the user's price.
quantity: An integer representing the user's quantity.

UserAddress Model
city: A string representing the city in the user's address.
country: A string representing the country in the user's address.
zipcode: An integer representing the zipcode in the user's address.

OrderItem Model
productId: A string representing the ID of the product in an order item.
boughtQuantity: An integer representing the quantity of the product bought in an order item.

Order Model
timestamp: A datetime object representing the timestamp of the order.
items: A list of OrderItem objects representing the items included in the order (default is an empty list).
total_amount: A float representing the total amount of the order.
address: An object of type UserAddress representing the user's address associated with the order.
```

```
routes/user.py

This code defines API routes for handling user products and orders using FastAPI.

/product Endpoints:
GET /product: Retrieves all products from the database.
POST /product: Creates a new product and adds it to the database.
PUT /product/{id}: Updates an existing product with the specified ID.
DELETE /product/{id}: Deletes a product with the specified ID.

/order Endpoints:
GET /order: Retrieves all orders from the database.
POST /order: Creates a new order and adds it to the database.
PUT /order/{id}: Updates an existing order with the specified ID.
DELETE /order/{id}: Deletes an order with the specified ID.

Usage:
The code utilizes the PyMongo connection object conn to interact with the MongoDB database.
Data is serialized to and deserialized from dictionaries using serializeDict and serializeList functions from schemas.user.
The datetime module is used to timestamp orders.
The bson module is used to work with MongoDB ObjectIds for querying and updating records.
```

```
schemas/user.py

This code defines two methods for serializing data to JSON format.

userEntity(item) -> dict

Parameters:
item: A dictionary representing a user entity.
Returns:
A dictionary with the following key-value pairs:
"id": The string representation of the "_id" field from the input dictionary.
"name": The value associated with the "name" key from the input dictionary.
"price": The value associated with the "price" key from the input dictionary.
"quantity": The value associated with the "quantity" key from the input dictionary.

usersEntity(entity) -> list

Parameters:
entity: A list of dictionaries representing user entities.
Returns:
A list of dictionaries, where each dictionary is obtained by applying the userEntity function to each item in the input list.

serializeDict(a) -> dict

Parameters:
a: A dictionary to be serialized.
Returns:
A new dictionary where:
The keys are retained as-is (except for the "_id" key, which is converted to a string).
The values are converted to strings if the key is "id", and they are retained as-is for other keys.

serializeList(entity) -> list

Parameters:
entity: A list of dictionaries to be serialized.
Returns:
A list of dictionaries, where each dictionary is obtained by applying the serializeDict function to each item in the input list.

These methods are used for transforming data structures, particularly when interacting with JSON data, by converting MongoDB ObjectId to strings and optionally converting other values to strings for serialization purposes
```

```
main.py

This code sets up a FastAPI application and includes a router for handling user-related routes.

app - FastAPI Application
An instance of the FastAPI application is created and assigned to the variable app.

app.include_router(user)
The user router, defined in routes.user, is included in the FastAPI application. This means that the routes defined in the user router will be accessible under the application's base URL.

This code serves as the foundation for creating an API that handles user-related operations using FastAPI. The specific routes and functionality for handling users are defined in the routes.user module.
```

![FastAPI-Python-MongoDB-logos](https://miro.medium.com/v2/resize:fit:1358/1*ETIV2puverF1etw9773pnA.jpeg)
