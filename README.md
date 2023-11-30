# microblog

### API
Installing API sources in development mode
```commandline
pip install -e '.[dev]'
```
Running API
```commandline
uvicorn api.app:create_app --host 127.0.0.1 --port 8000
```
Swagger UI will be available @ http://127.0.0.1:8000/docs
### API response prototype
```json
{
  "links": {
    "self": "http://microblog.com/posts?start=0&count=2",
    "next": "http://microblog.com/posts?start=2&count=5"
  },
  "data": [{
    "id": "7",
    "attributes": {
      "author": {
        "id": "213",
        "attributes": {
          "name": "Greg",
          "avatar": {
            "src": "http://microblog.com/users/avatars/Greg.png"
          }
        }  
      },
      "body": "Bajojajo",
      "created": "2023-04-20T18:34:59.000Z",
      "media": []
    }
  }, {
    "id": "13",
    "attributes": {
      "author": {
        "id": "411",
        "attributes": {
          "name": "Mediocrates",
          "avatar": {
            "src": "http://microblog.com/users/avatars/Mediocrates.png"
          }
        }
      },
      "body": "Eh... good enough",
      "created": "2023-11-07T23:20:47.000Z",
      "media": [{
          "type": "image",
          "src": "http://microblog.com/posts/13/image1.jpg"
        }, {
          "type": "video",
          "src": "http://microblog.com/posts/13/movie1.mp4"
        }
      ]
    }
  }]
}
```

### API request prototype for adding a post
```json
{
  "data": {
    "type": "posts",
    "attributes": {
      "body": "Bajojajo",
      "media": [
        "<Some link to uploaded image>",
        "<Some link to uploaded image>",
        "<Some link to uploaded image>"
      ]
    }
  }
}
```
