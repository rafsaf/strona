#!/bin/bash

cd ~/Tribal-Wars-Planer

git fetch
git reset --hard HEAD
git merge origin/master

docker image prune --force
set +e
sudo docker-compose -f docker-compose.stg.yml pull && sudo docker-compose -f docker-compose.stg.yml up -d
docker image prune --force