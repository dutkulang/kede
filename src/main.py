from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

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
def posts(limit:Optional[int] = 10, published:Optional[bool] = True):
    """
    Retrives all posts

    Args:
        limit : int [Optional], fetch 10 posts by default
        published: bool [Optional], gets only published posts by default

    Returns:
        dict: A dictionary containing all the posts.
    """
    if published:
        return {
            'details': f'{limit} published posts',
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
    else:
        return {
            'details': f'{limit} unpublished posts'
        }

@app.get('/posts/{id:int}')
def post_detail(id: int) -> dict:
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

@app.get('/posts/{post_id}/comments')
def post_comments(post_id: int):
    """
    Handle comments on a post

    Args:
        post_id: id for the post whose comments are being retrived

    Returns:
        dict: A dictionary containing the posts details
        and comments. limit comments to the first 10 comments
        on a post.
    """
    return {
        'post':{
            'post_id': post_id,
            'comments': [
                {'details': 'hello a test comment'},
                {'details': 'test comment'}
            ]
        }
    }

class Post(BaseModel):
    title: str
    body: Optional[str] = None
    published : bool = False
@app.post('/post')
def post(post: Post):
    return post