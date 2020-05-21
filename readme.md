# Temperature sensor with led warning project

## Description
This application runs on a Raspberry Pi Zero W and a breadboard. The sensor data is displayed on a website powered by Django and Celery.

This project can be ported to other Raspberry Pi machines with more hardware resources if needed. 

The Django framework helps creating a quick web server and Celery is a Distributed Task Queue as the developer himself calls it, which helps the server-side tasks to be asynchronous and boost its response time.

## Getting Started

### Setup the breadboard and I/O pins

![Raspberry pi setup](https://i.ibb.co/qJShbz9/Annotation-2020-05-21-114706.jpg)

The setup for this project is pretty simple. As it is displayed above, the electronic parts you need for this are: Raspberry Pi(any version), one led, one DHT11 module, 2 resistors(1k and 10k ohm), 4 male/female wires and 4 male/male wires for breadboard connection.

### Installing

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

This command should run the python3 interpreter, if it exists, then the quit() method exits it.

If not found, installing the python3 interpreter should be easy:
```
    $ sudo apt-get install python3
```

Let's not forget about the module for the temperature sensor to help it get data from environment.
```
    $ sudo pip3 install Adafruit_DHT
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

### Running the application

After all those required packages installed, we need to run a celery worker. Enter the app folder and execute:
```
    $ sudo celery -A temp_website -l info -n worker
```
If you consider usefull runing more than one worker on the machine, it is possible. Just run the previous command with a different name in the "-n" argument. The workers will automatically syncronize.

Run the django project from the app folder with:
```
    $ sudo python3 manage.py runserver ip:80
```

The ip bit in the command should be the local IPv4 of the machine you are running this app on. If it is hard to find out your local network IPv4 run those command (returns 127.0.0.1 on machines having the hostname in /etc/hosts as 127.0.0.1):
```
    $ python3
    >>>import socket
    >>>socket.gethostbyname_ex(socket.gethostname())[-1][-1]
```

Browse to /temp_website/settings.py and add your IPv4 address to the ALLOWED_HOSTS list.

## Acknowledged problems

- Using this build is resource demanding, it may be not optimal to be run on a Raspberry Pi Zero W as the response times can be high.

- Also using the multiprocessing tool on a single threaded computer doesn't bring the best result.

- The sensor is a cheap version and even if it displays precision of one(one decimal digit), the measure isn't that precise.

## Resources and references

[Django documentation](https://towardsdatascience.com/image-panorama-stitching-with-opencv-2402bde6b46c)

[Celery documentation](https://docs.celeryproject.org/en/stable/)