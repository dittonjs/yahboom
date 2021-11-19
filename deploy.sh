#!/usr/bin/env bash

# remove old src zip
rm src.tar.gz

# zip up src directory
tar -zcvf src.tar.gz src

echo "Deploying"
scp src.tar.gz pi@192.168.50.1:~/python/src.tar.gz

echo "Installing"
ssh pi@192.168.50.1 "cd ~/python; rm -rf src; tar -xvzf src.tar.gz; rm src.tar.gz;"

echo "Deploy complete! run 'ssh pi@192.168.50.1' to remote into robot"

