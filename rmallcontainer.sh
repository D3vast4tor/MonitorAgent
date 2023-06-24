#!/bin/bash

for container in $(sudo docker ps -a --format {{.ID}})
do
    sudo docker stop $container
    sudo docker rm $container
done

for image in $(sudo docker image ls --format {{.ID}})
do
    sudo docker image rm $image --force
done

