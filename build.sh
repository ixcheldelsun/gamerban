#!bin/bash
set -o errexit

pip install --upgrade pip && pip install -r requirements.txt
python app/manage.py migrate