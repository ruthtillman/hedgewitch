#!/bin/bash

# To use this file, place it in the directory where you expect the files to exist. Create a list of the files you expect to find in the directory and save it as "expectedFileList.txt" in the directory (or be sure to change the path below). It will automatically generate the filesNotFound.txt, so you don't need to create that on your own.

# Make the file executable by running `chmod u+x checklist.sh`

# Execute by running `./checklist.sh`

for file in $(cat expectedFileList.txt) # Be sure this matches the name of your list of files you expect to find.
do
  if [ -f "$file" ]
  then
  	: 
  else
  	echo "$file" >> filesNotFound.txt # This will create the file if it doesn't already exist
  fi
done