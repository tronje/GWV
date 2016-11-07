#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Invalid arguments!"
    exit 1
fi

name=$1_04_Joergensen_Wille_Krabbe
cp -r $1 $name

echo "Creating tar ball..."
tar -X archive_exclude.txt -cvf $name.tar $name

rm -r $name

echo "Gzipping tar ball..."
gzip -9 -f $name.tar

echo "Created $name.tar.gz"
echo "Done!"

exit 0
