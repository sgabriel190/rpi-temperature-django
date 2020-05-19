# Temperature sensor with led warning project
## Author: Strilciuc Gabriel

## Description
This application runs on a Raspberry Pi Zero W and a breadboard. The sensor data is displayed on a website powered by Django and Celery.

The Django framework helps creating a quick web server and Celery is a Distributed Task Queue as the developer himself calls it, which helps the server-side tasks to be asynchronous and boost its response time.

## Prerequisites

This project uses django and celery, therefore the raspberry pi machine should have those installed.

I recommend running it on python3. 

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




## Installation
