import os 
from celery import Celery
from kombu import Exchange, Queue
from celeryRabbitMqApp.config import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryRabbitMqProject.settings')

item_queue_name = queueName
item_exchange_name = exchangeName
item_routing_key = routingKey

app = Celery('celeryRabbitMqProject',broker = rabbitMqUrl)
app.config_from_object('django.conf:settings',namespace='CELERY')

default_exchange = Exchange(item_exchange_name, type='')

item_queue = Queue(item_queue_name,default_exchange,routing_key=item_routing_key)

app.conf.task_queues = (item_queue,)

app.autodiscover_tasks()
