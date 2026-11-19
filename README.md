This project contains test .env file.
Author informed about risks of uploading real .env files in profuction ;)

To test an app, just rename .env-example into .env and run 2 commands:

# Building docker-image and container from Dockerfile 
docker build -t <image name you wish> .

# Runing docker container
docker run --name <container name you wish> <image namefrom previous commnand>
