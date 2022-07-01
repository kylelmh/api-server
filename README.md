# api-server
graphql server running on django + graphene + postgres, used for hosting JSONs of a CV

Play with a live example on [api.kylelmh.dev](https://api.kylelmh.dev/#query=%0Aquery%20a%20%7B%0A%20%20cvOf(name%3A%20%22Lee%22)%7B%0A%20%20%20%20firstName%0A%20%20%7D%0A%7D&operationName=a)

# setup locally:
```
docker-compose up --build
```

# deployment

```
# intended to be used with a reverse proxy
docker-compose -f docker-compose.prod.yml up
```
