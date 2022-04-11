#!/bin/bash
# A script to install dependencies

filename='requirements.txt'
n=1
while read line; do
# reading each line
echo "$line"
n=$((n+1))
done < $filename

python main.py