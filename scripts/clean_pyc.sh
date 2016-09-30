#!/bin/bash

find . -type f -iname '*.pyc' -print0 | xargs -0 -n1 rm
find . -type f -iname '*.pyo' -print0 | xargs -0 -n1 rm
