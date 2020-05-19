# Temperature sensor with led warning project
## Author: Strilciuc Gabriel

## Description
This application runs on a Raspberry Pi Zero W and a breadboard. The sensor data is displayed on a website powered by Django and Celery.

This project can be ported to other Raspberry Pi machines with more hardware resources if needed. 

The Django framework helps creating a quick web server and Celery is a Distributed Task Queue as the developer himself calls it, which helps the server-side tasks to be asynchronous and boost its response time.

## Getting Started

## Installing

This project uses django and celery, therefore the raspberry pi machine should have those installed. I recommend running them on python3. 

First, you need to make sure the machine is updated, for this run in a terminal those commands:
```
    $ sudo apt-get update
    $ sudo apt-get upgrade
```

Check if you have python3 installed by running in command line:
```
    $ python3
    >>>quit()
```

The first command should run the python3 interpretor, if it exists, then the quit() method exits it.

If not found, installing the python3 interpretor is not hard:
```
    $ sudo apt-get install python3
```

With those installed, proceed to install django and celery:
```
    $ sudo pip3 install django
    $ sudo pip3 install celery
```

I recommend installing those with sudo privileges, because we need sudo for running the website on HTTP port 80. Also rebooting the machine can be an option here, but not needed.

The celery framework needs a message broker: redis or rabbitMQ are one of those.

Installing redis:
```
    $ sudo apt-get install redis
    $ sudo pip3 install redis
```

## Running the application

After all those required packages installed, we need to run a celery worker. Enter the app folder and execute:
```
    $ sudo celery -A temp_website -l info -n worker
```

Run the django project from the app folder with:
```
    $ sudo python3 manage.py runserver ip:80
```