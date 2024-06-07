#---Advantages of fastApi
#1 inbuilt data validation
# 2 inbuilt documentation support,    3 fast
# 4 compact code - less time to write code,    5 less bugs
from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

class available_cuisine(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

@app.get("/")
def index():
    return "First Page !!"

#path parameters
@app.get("/hello/{name}")
async def hello(name):
    return f"welcome {name} !!"

food_items = {'indian' : ["Samosa", "Dosa"],
              'american' : ["Hot dog", "Apple Pie"],
              'italian' : ["Ravioli", "pizza"]}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: available_cuisine):
    return food_items.get(cuisine)

#query parameters
#url -- http://127.0.0.1:8000/page?no=4&done=True
@app.get("/page")
def page(no=1, done: bool = False, star: Optional[int] = None):
    if star:
        return f"Page no. {no} and it is already visited - {done} and has {star} star rating."
    else:
        return f"Page no. {no} and it is already visited - {done}"


#post request
@app.post("/blog")
def create_blog():
    return {'data': "Blog is created"}