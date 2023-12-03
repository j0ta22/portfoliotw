#!/usr/bin/env bash
# exit on error
set -o errexit

npm i -g yarn
npm i -g rimraf
npm install cross-env
pip install -r ./portfolio/requirements.txt 
python ./portfolio/manage.py collectstatic --no-input
python ./portfolio/manage.py migrate
python ./portfolio/manage.py tailwind build 