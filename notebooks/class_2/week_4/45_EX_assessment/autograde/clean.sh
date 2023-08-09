#!/usr/bin/bash
find ./ -type d \( -name '__pycache__' -o -name '.pytest_cache' \) -exec rm -rf {} +;
rm -f log.xml
