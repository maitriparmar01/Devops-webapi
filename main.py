# first step pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#class PostHello(BaseModel):
#    name:str
#    age:int

@app.get("/hello")
def hello_world():
    return {"message": "hello, World!"}

#@app.get("/hello/{name}/{age}")
#def hello_world(name:str, age:int):
#    print("data ->" , name, age)
#    return {"message": f"Hello , {name}+{age}"}

#@app.get("/hello")
#def hello_world(name:str, age:int):
#    print("data ->" , name, age)
#    return {"message": f"Hello , {name}"}

#@app.post("/hello")
#def hello_world():
#    return {"message": "hello, World!"}

#@app.post("/hello")
#def hello_world(post_hello: PostHello):
#    print("data->", post_hello)
#    return {"message": f"Hello, {post_hello.name}+{post_hello.age}"}

    
