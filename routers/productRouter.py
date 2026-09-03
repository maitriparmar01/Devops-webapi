from fastapi import APIRouter, Response
from controller.productController import create_product_controller, get_product_controller, get_product_by_id_controller, delete_product_controller, update_product_controller
from models.productModel import Product

productRouter = APIRouter( 
    prefix = "/products",
    tags = ["products"]
)

@productRouter.post("/postproduct")
async def create_product(product: Product, response: Response):
    return await create_product_controller(product, response)

@productRouter.get("/getproducts")
async def get_product(response: Response):
    return await get_product_controller(response)

@productRouter.get("/getproduct/{productid}")
async def get_product(productid: str, response: Response):
    return await get_product_by_id_controller(productid,response)

# Delete product
@productRouter.delete('/deleteproduct/{productid}')
async def delete_product(productid: str, response: Response):
    return await delete_product_controller(productid,response)

# Update product
@productRouter.put('/updateproduct/{productid}')
async def update_product(productid: str, product: Product, response: Response):
    return await update_product_controller(productid,product,response)

#@productRouter.get("/getproduct/{productid}")
#def get_product(productid: int, response: Response):
#    try:
#        response.status_code = 200
#        for product in products:
#            if product.id == productid:
#               return {"product": product, "isSuccess": True}
#            
#        response.status_code = 404
#        return {"message": "Product not found", "isSuccess": False}
#    except Exception as e:
#        print(e)
#        response.status_code =500
#        return {"message": "Error fetching product", "isSuccess": False}
    
#@productRouter.put("/product/{productid}")
#def UpdateProduct(productid, products : Product, response: Response):
#    try:
#        idx = 0 
#        for index in range(0, len(products), 1):
#            if products[index] == productid:
#                idx = index
#            response.status_code = 200
#            return {"message": "Product Updated Succesfully", "isSuccess": True}
        
#        productid[idx] = products
#        response.status_code = 404
#        return {"message": "product not found","isSuccess": False}

#@app.delete("/product/{productid}")
#def DeleteProduct(productid: int, response: Response):
    try:
        for index in range(0, len(products)):
            if products[index].id == productid:
                
                deleted_product = products.pop(index)
                
                response.status_code = 200
                return {
                    "isSuccess": True,
                    "message": "Product deleted successfully!",
                    "product": deleted_product
                }

        response.status_code = 404
        return {
            "message": "Product not found",
            "isSuccess": False
        }

    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "message": "Error deleting product",
            "isSuccess": False
        }

# Update and delete assignment

