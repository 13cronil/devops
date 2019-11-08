#!/bin/sh

docker login -u $DOCKER_USERNAME -p $DOCKER_PWD
TAG="latest"

docker build -t scrape-bbc:$TAG .
docker push scrape-bbc:$TAG
