#!/usr/bin/env bash
# exit on error
set -o errexit


npm cache clear --force
npm i -g yarn
npm i -g rimraf
npm install cross-env
npm update
npm install -g tailwindcss
pip install -r ./portfolio/requirements.txt 
python ./portfolio/manage.py collectstatic --no-input
python ./portfolio/manage.py migrate
python ./portfolio/manage.py tailwind build 