# kede
Kede an South Sudanese social media platform.

```bash
# first install fastapi and uvicorn

pip3 install fastapi uvicorn
```

```py
# ./main.py

from fastapi import FastAPI

app = FastAPI # create an instance of FastAPI

@app.get('/') # defines path method and routes to '/'
def index():
    """
    handle homepage path routes

    Args:
        None
    
    Returns:
        dict: with string values
    """
    return {
        'info': 'index page'
    }

def about():
    return {
        'info': 'about page'
    }

```

`@app.get('/')`:
    path operation decorator <br>
    `get` is the operation function/method with path as a string.