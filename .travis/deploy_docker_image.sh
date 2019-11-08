#!/bin/sh

docker login -u $DOCKER_USERNAME -p $DOCKER_PWD
TAG="latest"

docker build -t $DOCKER_USERNAME/scrape-bbc:$TAG .
docker push $DOCKER_USERNAME/scrape-bbc:$TAG
