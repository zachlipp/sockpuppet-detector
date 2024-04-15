# Sock Puppet Detector

## Running

`docker compose --profile run up --build`

The service's endpoint is `http://localhost:1337/`, and because this is built with `FastAPI`, the docs are viewable at `http://localhost:1337/redoc`.

## Testing

### With `pytest`

`docker compose --profile test up --build`

### With `curl`

Because this service uses `GET` requests in a nonstandard way (passing JSON data), we are unable to use `FastAPI`/`Starlette`'s `TestClient` to coordinate our integration tests. So to run a true end-to-end example, run the container with the `run` profile, and then use `curl` to send data. That is:

`docker compose --profile run up -d --build`

And then:

`curl -X GET http://localhost:1337 -H "content-type: application/json" --data @payload.json`

which returns:

`{"similar_names":[["lebron_number_one_goat","lebron_number_one_goooatt",0.88]]}`
