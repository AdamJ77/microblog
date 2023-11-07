### **API response prototype**
```json
{
  "data": [{
    "type": "posts",
    "id": "7",
    "attributes": {
      "body": "Bajojajo",
      "created": "2023-04-20T18:34:59.000Z",
      "media": [
        "http://microblog.com/posts/7/image1.png",
        "http://microblog.com/posts/7/image2.png",
        "http://microblog.com/posts/7/image3.png"
      ]
    },
    "relationships": {
      "author": {
        "data": { "type": "users", "id": "213" }
      }
    }
  }, {
    "type": "posts",
    "id": "13",
    "attributes": {
      "body": "Eh... good enough",
      "created": "2023-11-07T23:20:47.000Z",
      "media": [
        "http://microblog.com/posts/13/image1.png",
        "http://microblog.com/posts/13/image2.png"
      ]
    },
    "relationships": {
      "author": {
        "data": { "type": "users", "id": "411" }
      }
    }
  }],
  "included": [{
    "type": "users",
    "id": "213",
    "attributes": {
      "name": "Greg",
      "avatar": {
        "src": "http://microblog.com/users/avatars/Greg.png"
      }
    }
  }, {
    "type": "users",
    "id": "411",
    "attributes": {
      "name": "Mediocrates",
      "avatar": {
        "src": "http://microblog.com/users/avatars/Mediocrates.png"
      }
    }
  }]
}
```
