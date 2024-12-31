
# After installing the fastapi library(module) , we can import this library(module) in our python file 
    # and create a web application using fastapi library(module). 

# To create a web application using fastapi library(module) , we need to follow some steps :

    # Step 1 : Import the fastapi library(module) in python file.
    # Step 2 : Create an instance of FastAPI class.
    # Step 3 : Define the routes using decorators like @app.get() , @app.post() , @app.put() , @app.delete() etc.
    # Step 4 : Define the functions for each route which will return the response to the client request using return statement.
    # Step 5 : Run the web application using uvicorn server in command prompt or terminal using command 'uvicorn filename:app --reload'.
    # Step 6 : Open the browser and type the url 'http:// 
    # Step 7 : Hit the enter button , you will see the response in the browser.
    # Step 8 : If you want to stop the server then press "control + c" in command prompt or terminal where the server is running. 


## Let's create a web application using fastapi library(module) in python file.
    #  https://pypi.org/project/fastapi/

# Step 1 : Import the fastapi library(module) in python file.

from typing import Union               # 'Union' is a class used to define the type of the variable , it can be of any type like int , float , str etc.
from fastapi import FastAPI
import uvicorn

# Step 2 : Create an instance of FastAPI class.

app = FastAPI()

# Step 3 : Define the routes using decorators like @app.get() , @app.post() , @app.put() , @app.delete() etc.
@app.get("/")

# Step 4 : Define the functions for each route which will return the response to the client request using return statement.
async def read_root():
    return {"Hello": "World"}

#  
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# if we want to run the web application using uvicorn server then we need to write the below code.

if __name__ == "__main__":       # '__name__' is a special variable in python which will be equal to '__main__' if the python file is executed directly , 
    uvicorn.run(app, host="0.0.0.0", port=8080)  # app_run() is a function used to run the web application , it takes 3 arguments , 1st is instance of FastAPI class , 2nd is host , 3rd is port number.
                                                # 'host' is the ip address of the server where the web application is running .
                                                # 'port' is the port number where the web application is running like 8080 , 5000 etc.

# Step 5 : Run the web application using uvicorn server in command prompt or terminal using command 
    #  'python 12.pip_in_python.py' or 'python filename.py' or 'uvicorn filename:app --reload' or 'uvicorn filename:app --reload --port 8080' 

# Step 6 : Open the browser and type the url 'http://

# Step 7 : Hit the enter button , you will see the response in the browser.

# Step 8 : If you want to stop the server then press "control + c" in command prompt or terminal where the server is running.
