import random


from .app import celery_app
from .coingecko import coingecko_periodic_task


celery_app.conf.beat_schedule = {
    'my_periodic_task': {
        'task': 'tasks.coingecko.coingecko_periodic_task',
        'schedule': random.randint(10, 20),
    },
}
celery_app.conf.timezone = 'UTC'
