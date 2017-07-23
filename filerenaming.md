# Scripts to Handle Problems in Filenames

## Scripts for Substitution in Filenames

Note, the way these scripts currently work, they'll only change the first instance of the issue in your filename. The easiest way to check if any still exist in the directory (and note, this will also check subdirectories) is to run:

`find . -name "*wordOrSpace*" | wc -l`

where wordOrSpace is the word or space you're looking for. This will give you an output count of how many files it still appears in. Normally, when I'm fixing something like a space, 

Would love to see a simplified form which hits them all in one go, but it's easier to run this 5x quickly, check for any remaining filenames with spaces, and move on, than it is to completely rewrite it.

## A script to substitute one word for another in your filenames

**Note: This script will not properly operate on files which have spaces in their filenames, see below**

Where "Lebenen" is the misspelled word you want to change to "Lebanon" in this situation.

`for badfile in $(find . -name "*Lebenen*"); do mv "$badfile" "`echo $badfile | sed 's/Lebenen/Lebanon/'`"; done`

_again, note, it only changes this once, so you'd run it twice if you expected to find it more than once_

You can use the same format to switch all your underscores to hyphens, e.g.

`for badfile in $(find . -name "*_*"); do mv "$badfile" "`echo $badfile | sed 's/_/-/'`"; done`

or vice-versa:

## A script to remove spaces or ampersands from your filenames

Note, the "find" method returns filenames differently and in a way that doesn't work well for handling spaces or ampersands.

Spaces: `for f in *; do mv "$f" "`echo $f | sed s/\ /_/`"; done`

Ampersands: `for f in *; do mv "$f" "`echo $f | sed s/\&/_/`"; done`

You can do it with other special characters as well.

You can change the * into *.jpg or any extension if you're only targeting one kind of file. It will return errors for every filename which doesn't contain the issue.

To test whether any files in the directory still contain spaces, run:

`find . -name "* *" | wc -l`