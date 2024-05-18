#!/bin/bash

counter=$1
while [ $counter -gt 0 ]
do
   counter=$(( $counter - 2 ))
   python arg_bash.py  $(( $counter  )) &
done
echo "$1 Consumers launched"