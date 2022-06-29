# api-server
graphql server running on django + graphene + postgres

# setup locally:
```
docker-compose up --build
```

# deployment

```
# intended to be used with a reverse proxy
docker-compose -f docker-compose.prod.yml up
```
