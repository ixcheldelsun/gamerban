#!/bin/bash

# This script is used to deploy the application to the server
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build