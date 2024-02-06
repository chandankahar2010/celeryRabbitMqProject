from celery import shared_task
from time import sleep
from celeryRabbitMqApp.models import Items

@shared_task()
def consumerItem(item,id):
    sleep(20)  # used sleep of 20s to check pending status
    Items.objects.filter(id=id).filter(status='Pending').update(status =  'Completed')
    response = {}
    response["status_code"] = "203"
    response["message"] = "status updated successfully!"
    return response