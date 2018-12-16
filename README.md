# startmeapp-hackathon

## Development

Run the following commands to start the container locally:

1. `docker build -t startmeapp:local .`
1. `docker run -p 5000:5000 -v $(pwd):/usr/app startmeapp:local`