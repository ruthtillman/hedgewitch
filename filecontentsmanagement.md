# Scripts to Manage the Contents of Files

## A Script to Substitute Basic Strings in a File
 
To replace one string with another in all files in the directory, where the string to be found is "dc:creator#author" and the string to replace it with is "mrel:aut" run:

`for f in $(ls); do sed -i -e 's/dc:creator#author/mrel:aut/g' $f; done`

Note: Exercise careful consideration of what you're finding and replacing. If you replace "placing" with "putting" you will also replace "replacing" with "reputting."