#!/bin/sh

cd src
gunicorn asgi:app --preload --bind 0.0.0.0:8000 --workers 4 --worker-class uvicorn.workers.UvicornWorker