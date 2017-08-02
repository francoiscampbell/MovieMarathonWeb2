#!/usr/bin/env bash -e

TAG='gcr.io/moviemarathon-1495982743507/moviemarathon'
KEY_FILE=${HOME}/gcp-key.json
echo ${GOOGLE_AUTH} | base64 -i --decode > ${KEY_FILE}
echo ${NGINX_CONF} | base64 -i --decode > deploy/default.conf
docker build -t ${TAG} -f deploy/Dockerfile-prod deploy
gcloud auth activate-service-account --key-file ${KEY_FILE}
gcloud docker -- push ${TAG}
ssh campbell.francois@moviemarathon.ca "
    /tmp/google-cloud-sdk/bin/gcloud docker -- pull $TAG:latest &&
    docker rm \$(docker stop \$(docker ps -aq)) &&
    docker run -d -p 80:80 $TAG:latest
    echo restarted
    "