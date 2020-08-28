sudo python3 manage.py runserver 192.168.0.107:80 &> ./logging/django_logger.log &
sudo celery -A temp_website -l info -n worker1 &> ./logging/celery_worker1_logger.log &
sudo celery -A temp_website -l info -n worker2 &> ./logging/celery_worker2_logger.log &