#!/bin/bash

DIRNAME=$(dirname $0)
cd $DIRNAME

docker-compose down

images=$(docker images | grep mlops | awk -F ' ' '{print $1":"$2}')
echo "Warning! This will remove the following images"
echo $images
echo -n "Do you want to proceed? [y/n]"
read decision
if [ -z $decision ]; then
  exit 0
fi
if [ $decision = 'y' ]; then 
  echo "Removing images"
  echo $images
  docker rmi $images 2> /dev/null 
fi
exit 0
