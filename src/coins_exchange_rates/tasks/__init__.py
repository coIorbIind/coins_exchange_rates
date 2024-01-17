from .app import celery_app
from .coingecko import coingecko_periodic_task


celery_app.conf.beat_schedule = {
    'my_periodic_task': {
        'task': 'tasks.coingecko.coingecko_periodic_task',
        'schedule': 4,
    },
}
celery_app.conf.timezone = 'UTC'
