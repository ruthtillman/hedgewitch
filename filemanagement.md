# Scripts for Managing Your Files

## A Script to Check Whether Expected Files are in a Directory

In a lot of larger-scale metadata/file work, it may be impossible to perform visual verification that the expected files are in a directory. The checklist script in `/bash/checklist.sh` will run against a list you've given it of filenames you expect to be in the directory. This list should have linebreaks or spaces as delimiters between filenames. If the file is not found, it will add it to a text file. If all files are found, the text file will not be created. It won't tell you about additional files it's found.

### To use it

To use `checklist.sh`, place it in the directory where you expect the files to exist. Create a list of the files you expect to find in the directory and save it as `expectedFileList.txt` in the directory (or elsewhere and change the path to it in `checklist.sh`. It will automatically generate the `filesNotFound.txt` in the working directory, so you don't need to create that on your own. You can modify the script to work from outside the directory.

Make the file executable by running `chmod u+x checklist.sh`

Execute by running `./checklist.sh`