#!/bin/sh

cd src

PYTHONPATH="/app/src/coins_exchange_rates"

celery --app=tasks.app:celery_app worker -B -l INFO
