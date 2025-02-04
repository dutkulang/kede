from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="A simple API to demonstrate FastAPI documentation improvements.",
    version="1.0.0",
    contact={
        "name": "Dut",
        "email": "dutkulang@kede.com",
    },
    license_info={
        "name": "MIT",
    },
)

@app.get('/')
async def home():
    """
    Handle request to '/' path

    Args:
        None
    
    Returns:
        dict: A dictionary with a success message

    """
    return {
        'info': 'API connection success'
    }

@app.get('/about')
async def about():
    """
    Handles requests to the about page

    This endpoint provides information about the API

    Args:
        None

    Returns:
        dict: A dictionary containing information about the API 

    """
    return {
        'info': 'The about page'
    }

@app.get('/posts')
def posts():
    """
    Retrives all posts

    Args:
        None

    Returns:
        dict: A dictionary containing all the posts.
    """
    return {
        'posts': 
            [
                {
                    'title':'Introduction to C',
                    'id': 1,
                    'author': 'Dut'
                },
                {
                    'title':'Java for dummies',
                    'id': 2,
                    'author': 'Garang John'
                },
                {
                    'title':'Django for beginners',
                    'id': 3,
                    'author': 'Ben Sham'
                }
            ]
        }

@app.get('/posts/{id:int}')
def post(id: int) -> dict:
    """
    Retrive a post by id

    Args:
        post_id: id for post being requested for.

    Returns:
        dict: A dictionary containing details 
        about the requested post with the 
        provided id.
    """
    return {
        'post_id': id
    }