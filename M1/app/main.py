from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Dish(BaseModel):
    name: str
    ingredients: List[str]
    cuisine: str
    difficulty: str

dishes = [
    Dish(
        name="Spaghetti Bolognese",
        ingredients=["spaghetti", "ground beef", "tomato sauce", "onions"],
        cuisine="Italian",
        difficulty="easy"
    ),
    Dish(
        name="Pad Thai",
        ingredients=["rice noodles", "chicken", "peanuts", "bean sprouts"],
        cuisine="Thai",
        difficulty="medium"
    ),
    Dish(
        name="Hamburger",
        ingredients=["beef patty", "bun", "lettuce", "tomato", "onion"],
        cuisine="American",
        difficulty="easy"
    )
]



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/dishes/{dishName}")
async def read_dish(dishName):
    result = next(
        (dish for dish in dishes if dish.name == dishName),
        None
    )
    return {"dish": result}


@app.post("/dishes/")
async def create_dish(dish: Dish):
    dishes.append(dish)
    return dish

@app.get("/dishes/")
async def get_all_dishes():
    return {"dishes": dishes}

    