#!/bin/bash

echo Cleaning .pyc files...
find . -type f -iname '*.pyc' -print0 | xargs -0 -n1 rm
echo Cleaning .pyo files...
find . -type f -iname '*.pyo' -print0 | xargs -0 -n1 rm
echo Cleaning .swp files...
find . -type f -iname '*.swp' -print0 | xargs -0 -n1 rm
