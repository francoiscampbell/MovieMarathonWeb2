#!/usr/bin/env bash -e

TAG='gcr.io/moviemarathon-1495982743507/moviemarathon'
yarn run webpack
docker build -t ${TAG} -f ./deploy/Dockerfile-prod ./deploy
gcloud docker -- push ${TAG}
ssh campbell.francois@moviemarathon.ca "
    /tmp/google-cloud-sdk/bin/gcloud docker -- pull $TAG:latest &&
    docker rm \$(docker stop \$(docker ps -aq)) &&
    docker run -d -p 80:80 $TAG:latest
    echo restarted
    "