#!/bin/bash
mkdir tmp
cp run_application.py tmp/__main__.py
cp whisker.py tmp/
cd tmp
zip -r run_application.zip *.py
mv run_application.zip ../
cd ../
rm -rf tmp
