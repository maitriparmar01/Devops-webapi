from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    description: str

products = []

@app.post('/products')
def create_product(product: Product, response: Response):
    products.append(product)    
    response.status_code = 201
    return {"message": "Product created successfully", "product": product }

@app.get('/prodcuts')
def get_product(response: Response):
    print('Data-->', products)
    response.status_code = 200
    return{"message":"Product get successfully", 'Products' : products}