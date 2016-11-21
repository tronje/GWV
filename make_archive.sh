#!/bin/bash

# expect exactly one argument
if [ $# -ne 1 ]; then
    echo "Invalid arguments!"
    exit 1
fi

# name starts with first (and only) argument!
name=$1_04_Joergensen_Wille_Krabbe

# copy the directory with the given name
# to the newly generated name
cp -r $1 $name

echo "Creating tar ball..."

# tar it, excluding all files listed in archive_exclude.txt
tar -X archive_exclude.txt -cvf $name.tar $name

# remove the directory, we no longer need it
rm -r $name

echo "Gzipping tar ball..."

# gzip -9 for maximum compression
gzip -9 -f $name.tar

echo "Created $name.tar.gz"
echo "Done!"

exit 0
