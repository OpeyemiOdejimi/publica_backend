
# import bcrypt
# from database import db
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from sqlalchemy import text
# import os
# from dotenv import load_dotenv
# import uvicorn

# load_dotenv()


# app = FastAPI(title="Simple App", version="1.0.0")

# class simple(BaseModel):
#     name: str = Field(..., example= "Sam Larry")
#     email: str= Field(..., example= "oke@gmail.com")
#     password: str=Field(..., example= "ade121")

# @app.get("/", description="This endpoint just return a welcome message")
# def root():
#     return {"Message": "Welcome to my FastAPI App"}

# @app.post("/signup")
# def signUp(input:simple):
#     try:
#         duplicate_query=text(""" SELECT * FROM users WHERE email=:email """)
#         existing=db.execute(duplicate_query,{"email":input.email})
#         if existing:
#             print("Email already exist")
            
#             # raise HTTPException(status_code=400, detail="Email already exist")
#         query= text("""
#             INSERT INTO users (name, email, password)
#         VALUES(:name, :email, :password);
#         """)
#         # hashing password
#         salt=bcrypt.gensalt()
#         hashedpassword=bcrypt.hashpw(input.password.encode('utf-8'), salt)
#         print(hashedpassword)

#         # mapping data
#         data= {"name":input.name, "email":input.email, "password":hashedpassword}
#         db.execute(query,data)
#         db.commit()
#         return {"Message": "User created sucessfuly", "data":{"name":input.name, "email":input.email}}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=e)
# if __name__=="__main__":
#      uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))








import bcrypt
from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
load_dotenv()
app=FastAPI(title="Simple App", version="1.0.0")
class simple(BaseModel):
    name: str = Field(..., example= "Sherif Oke")
    email: str= Field(..., example= "oke@gmail.com")
    password: str=Field(..., example= "ade121")
@app.get("/", description="This endpoint just return a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI App"}
@app.post("/signup")
def signUp(input:simple):
    try:
        duplicate_query=text(""" SELECT * FROM users WHERE email=:email """)
        existing=db.execute(duplicate_query,{"email":input.email})
        if existing:
            print("Email already exist")
            # raise HTTPException(status_code=400, detail="Email already exist")
        query= text("""
            INSERT INTO users (name, email, password)
        VALUES(:name, :email, :password);
        """)
        # hashing password
        salt=bcrypt.gensalt()
        hashedpassword=bcrypt.hashpw(input.password.encode('utf-8'), salt)
        print(hashedpassword)
        # mapping data
        data= {"name":input.name, "email":input.email, "password":hashedpassword}
        db.execute(query,data)
        db.commit()
        return {"Message": "User created sucessfuly", "data":{"name":input.name, "email":input.email}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
if __name__=="__main__":
     uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))






