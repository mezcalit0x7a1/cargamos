# Cargamos - Store Testing
The following project is an inventory control test, implementing the Flask and Postgresql framework as a database.

### Seting up the project (Ubuntu 20.04)
```
$ git clone git@github.com:mezcalit0x7a1/cargamos.git
$ cd cargamos
$ python3.8 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ flask run
```

# API

## Stores
**- GET - /stores** 
Get all stores from database
````
# Response example
{
    "resource": [
        {
            "id": 1,
            "name": "El señor de la tienda",
            "address": "Se casa #400 col. Santa Fe",
            "city": "Puerto Morelos",
            "state": "Quintana Roo",
            "zip_code": "1234",
            "phone": "9981234567",
            "email": "sr.tienda@gmail.com"
        },
        {
            "id": 2,
            "name": "Tienda Esotérica",
            "address": "Brillo Nocturno #666 Col. Hogwarts",
            "city": "Puerto Morelos",
            "state": "Quintana Roo",
            "zip_code": "1234",
            "phone": "9986565412",
            "email": "esoterica@gmail.com"
        }
    ]
}
````

**- POST - /stores** 
Create new store
````
# JSON body request example
{
    "name": "La tienda de los deseos",
    "address": "Calle #13, col. Santiago",
    "city": "Puerto Morelos",
    "state": "Quintana Roo",
    "zip_code": "1234",
    "phone": "9986565412",
    "email": "deseos@gmail.com"
}

# Response example
{
    "resource": {
        "id": 8,
        "name": "La tienda de los deseos",
        "address": "Calle #13, col. Santiago",
        "city": "Puerto Morelos",
        "state": "Quintana Roo",
        "zip_code": "1234",
        "phone": "9986565412",
        "email": "deseos@gmail.com"
    }
}
````

**- GET - /stores/[id]** 
Get store by id
````
# Response example
{
    "resource": {
        "id": 5,
        "name": "Tienda su sagrada actualización",
        "address": "Test #987, col. Ceviche",
        "city": "Solidaridad",
        "state": "Quintana Roo",
        "zip_code": "1999",
        "phone": "9841256956",
        "email": "updated@gmail.com"
    }
}
````

**- DELETE - /stores/[id]** 
Delete store
````
# Response will return status 200
{}
````

**- PUT - /stores/[id]** 
Update store
````
# JSON body request example
{
        "name": "Tienda su sagrada actualización",
        "address": "Test #987, col. Ceviche",
        "city": "Solidaridad",
        "state": "Quintana Roo",
        "zip_code": "1999",
        "phone": "9841256956",
        "email": "updated@gmail.com"
    }

# Response will return status 204
````

## Branches
**- GET - /branches** 
Get all branches from database
````
# Response example
{
    "resource": [
        {
            "id": 1,
            "name": "Apple"
        },
        {
            "id": 3,
            "name": "Nike"
        },
        {
            "id": 2,
            "name": "Samsung"
        },
        {
            "id": 5,
            "name": "Steren"
        }
    ]
}
````

**- POST - /branches** 
Create new branch
````
# JSON body request example
{
    "name": "XRay"
}

# Response example
{
    "resource": {
        "id": 6,
        "name": "XRay"
    }
}
````

**- GET - /branches/[id]** 
Get branch by id
````
# Response example
{
    "resource": {
        "id": 6,
        "name": "Steren"
    }
}
````
**- DELETE - /branches/[id]** 
Delete branch
````
# Response will return status 200
{}
````

**- PUT - /branches/[id]** 
Update branch
````
# JSON body request example
{
    "name": "My branch"
}

# Response will return status 204
````

## Categories
**- GET - /categories** 
Get all categories from database
````
# Response example
{
    "resource": [
        {
            "id": 1,
            "name": "Smartphone"
        },
        {
            "id": 2,
            "name": "TV"
        },
        {
            "id": 3,
            "name": "Tennis"
        },
        {
            "id": 4,
            "name": "Tablet"
        },
        {
            "id": 6,
            "name": "Webcam"
        },
        {
            "id": 7,
            "name": "Laptop"
        }
    ]
}
````

**- POST - /categories** 
Create new category
````
# JSON body request example
{
    "name": "Shoes"
}

# Response example
{
    "resource": {
        "id": 16,
        "name": "Shoes"
    }
}
````

**- GET - /categories/[id]** 
Get category by id
````
# Response example
{
    "resource": {
        "id": 4,
        "name": "Tablet"
    }
}
````
**- DELETE - /categories/[id]** 
Delete category
````
# Response will return status 200
{}
````

**- PUT - /categories/[id]** 
Update category
````
# JSON body request example
{
    "name": "Laptop"
}

# Response will return status 204
````

## Products
**- GET - /products** 
Get all products from database
````
# Response example
{
    "resource": [
        {
            "id": 1,
            "name": "Iphone SE Rojo 60GB 2012",
            "branch": {
                "id": 1,
                "name": "Apple"
            },
            "category": {
                "id": 1,
                "name": "Smartphone"
            }
        },
        {
            "id": 4,
            "name": "Iphone SE Negro 60GB 2012",
            "branch": {
                "id": 1,
                "name": "Apple"
            },
            "category": {
                "id": 1,
                "name": "Smartphone"
            }
        },
        {
            "id": 6,
            "name": "Webcam USB Full HD COM-122",
            "branch": {
                "id": 5,
                "name": "Steren"
            },
            "category": {
                "id": 6,
                "name": "Webcam"
            }
        },
        {
            "id": 5,
            "name": "Macbook PRO MID 2012 Silver 500GB",
            "branch": {
                "id": 1,
                "name": "Apple"
            },
            "category": {
                "id": 7,
                "name": "Laptop"
            }
        }
    ]
}
````

**- POST - /products** 
Create new product
````
# JSON body request example
{
    "name": "Webcam USB Full HD COM-122",
    "id_category": 6,
    "id_branch": 5
}

# Response example
{
    "resource": {
        "id": 8,
        "name": "Webcam USB Full HD COM-122",
        "id_category": 6,
        "id_branch": 5
    }
}
````

**- GET - /products/[id]** 
Get product by id
````
# Response example
{
    "resource": {
        "id": 4,
        "name": "Iphone SE Negro 60GB 2012",
        "branch": {
            "id": 1,
            "name": "Apple"
        },
        "category": {
            "id": 1,
            "name": "Smartphone"
        }
    }
}
````
**- DELETE - /products/[id]** 
Delete product
````
# Response will return status 200
{}
````

**- PUT - /products/[id]** 
Update product
````
# JSON body request example
{
    "name": "Macbook PRO MID 2012 Silver 500GB",
    "id_category": 7,
    "id_branch": 1
}

# Response will return status 204
````

## StoreProducts
**- POST - /store_products** 
Asociate a product with a store and assing the stock, sku and price
````
# JSON body request example
{
    "sku": "WEBUSB9087234",
    "stock": 98,
    "price": 666,
    "product_id": 6,
    "store_id": 1
}

# Response example
{
	"id": 9,
    "sku": "WEBUSB9087234",
    "stock": 98,
    "price": 666,
    "product_id": 6,
    "store_id": 1
}
````

**- GET - /store_products/stores/[id]** 
Get the products that belong to a store
````
# Response example
{
    "resource": [
        {
            "id": 4,
            "sku": "SPISE2BL60",
            "stock": 37,
            "price": 12000.0,
            "product_id": 4,
            "store_id": 1
        },
        {
            "id": 9,
            "sku": "WEBUSB9087234",
            "stock": 98,
            "price": 666.0,
            "product_id": 6,
            "store_id": 1
        },
        {
            "id": 1,
            "sku": "SPISE2RED60",
            "stock": 0,
            "price": 12000.0,
            "product_id": 1,
            "store_id": 1
        }
    ]
}
````

**- PUT - /store_products/[id]** 
Edit a product store
````
# JSON body request example
{
	"sku": "SPISE2RED60",
	"stock": 0,
	"price": 12000.0,
	"product_id": 1,
	"store_id": 1
}

# Response will return status 204
````

**- PATCH - /store_products/[id]** 
Subtract product inventory
````
# JSON body request example
{
	"quantity": 3,
}

# Response returns 400 if stock is not available, otherwise returns 200
````

# Pytest
Tests are made to add stock to products with less than five products, then asynchronous requests are made to remove products until zero.
````
$ pytest -s

================================================================================== test session starts ===================================================================================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /var/www/html/cargamos
collected 6 items                                                                                                                                                                        

tests/test_flaskr.py Adding store products to id ---> 1
.....#0, Buy 2 items, Response code 200, Message -> , 60 In stock
#1, Buy 7 items, Response code 200, Message -> , 53 In stock
#2, Buy 1 items, Response code 200, Message -> , 52 In stock
#3, Buy 1 items, Response code 200, Message -> , 51 In stock
#4, Buy 7 items, Response code 200, Message -> , 44 In stock
#5, Buy 5 items, Response code 200, Message -> , 39 In stock
#6, Buy 1 items, Response code 200, Message -> , 38 In stock
#7, Buy 5 items, Response code 200, Message -> , 33 In stock
#8, Buy 7 items, Response code 200, Message -> , 26 In stock
#9, Buy 3 items, Response code 200, Message -> , 23 In stock
#10, Buy 6 items, Response code 200, Message -> , 17 In stock
#11, Buy 5 items, Response code 200, Message -> , 12 In stock
#12, Buy 3 items, Response code 200, Message -> , 9 In stock
#13, Buy 1 items, Response code 200, Message -> , 8 In stock
#14, Buy 1 items, Response code 200, Message -> , 7 In stock
#15, Buy 1 items, Response code 200, Message -> , 6 In stock
#16, Buy 6 items, Response code 200, Message -> , 0 In stock
#17, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#18, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#19, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#20, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#21, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#22, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#23, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#24, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#25, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#26, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#27, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#28, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#29, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#30, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#31, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#32, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#33, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#34, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#35, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#36, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#37, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#38, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#39, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#40, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#41, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#42, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#43, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#44, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#45, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#46, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#47, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#48, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#49, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#50, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#51, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#52, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#53, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#54, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#55, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#56, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#57, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#58, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#59, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#60, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#61, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#62, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#63, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#64, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#65, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#66, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#67, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#68, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#69, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#70, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#71, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#72, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#73, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#74, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#75, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#76, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#77, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#78, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#79, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#80, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#81, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#82, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#83, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#84, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#85, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#86, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#87, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#88, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#89, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#90, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#91, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#92, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#93, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#94, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#95, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#96, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#97, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#98, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#99, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#100, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#101, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#102, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#103, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#104, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#105, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#106, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#107, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#108, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#109, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#110, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#111, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#112, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#113, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#114, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#115, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#116, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#117, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#118, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#119, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#120, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#121, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#122, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#123, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#124, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#125, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#126, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#127, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#128, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#129, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#130, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
#131, Buy 4 items, Response code 400, Message -> Out of stock, ? In stock
#132, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#133, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#134, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#135, Buy 2 items, Response code 400, Message -> Out of stock, ? In stock
#136, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#137, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#138, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#139, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#140, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#141, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#142, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#143, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#144, Buy 1 items, Response code 400, Message -> Out of stock, ? In stock
#145, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#146, Buy 5 items, Response code 400, Message -> Out of stock, ? In stock
#147, Buy 3 items, Response code 400, Message -> Out of stock, ? In stock
#148, Buy 7 items, Response code 400, Message -> Out of stock, ? In stock
#149, Buy 6 items, Response code 400, Message -> Out of stock, ? In stock
.
````