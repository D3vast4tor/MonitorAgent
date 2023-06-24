#!/bin/bash

for volume in $(sudo docker volume ls --format {{.Name}})
do
    sudo docker volume rm $volume --force
done