### Prerequisites
1. Install Celery
First, install Celery using pip:


2. Install a Message Broker
Celery needs a message broker to send and receive messages. Install Redis with pip:

pip install redis

3. Configure Celery in Your Project
Create a celery.py File

Add a celery.py file to the project directory, i.e. celery_project > __init__.py:
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_project.settings")

app = Celery("celery_project")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

In your Django project directory create a file named celery.py

4. Start Redis Server
Make sure the Redis server is running. 

redis-server

5. Run Server 
Now you need to launch the Django test server:

python manage.py runserver

6. Run Celery Worker
Start the Celery worker to process tasks. Open a terminal window and run:

celery -A your_project_name worker --loglevel=info

7. Run Celery Beat
If you have periodic tasks and need Celery Beat to schedule them, run:

celery -A your_project_name beat --loglevel=i

