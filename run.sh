#!/bin/bash
# add .env file to the projects
cp backend/configs/.env.conf  backebd/.env &&


input="$1"
if [ "$input" = "development" ]; then
	echo "development mode..." &&
	echo "DO NOT USE IN ANY SERVER" &&
	echo "PROJECT ROOT DIR:" &&
	echo $(pwd) &&
	cp configs/docker-compose-development.conf docker-compose.yml &&
	cp backend/configs/Dockerfile-develop.conf back/Dockerfile &&
	echo "DONE"
elif  [ "$input" = "production" ]; then
	echo "production mode" &&
	cp configs/docker-compose-production.conf docker-compose.yml &&
	cp backend/configs/Dockerfile-deploy.conf back/Dockerfile &&
	echo "DONE"
else
  echo "You must specify the environment"
  break
fi

sudo docker-compose build &&
sudo docker-compose up --remove-orphans

