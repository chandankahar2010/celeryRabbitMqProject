# configuration for database
engineName = 'django.db.backends.sqlite3'
databaseName = 'db.sqlite3'

# configuration for celery 
rabbitMqUrl = 'amqp://guest@localhost:5672//'
queueName = 'queue1'
exchangeName = 'exchange1'
routingKey = 'queue1'