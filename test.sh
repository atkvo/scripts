#!/bin/bash

trap "echo 'hello'" SIGUSR1;

while true
do
    echo "HEY"
    sleep 1 
done

