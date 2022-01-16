

# Cloud Exam 2022


## 1. Section 1 

 
In this first section you are tasked to dockerize a simple python application that displays the following: 
- Your name
- Your school name 
- Your email

For this first section create the following directories: 
- docker
  - part1
  - part2
  - part3
  - part4


### 1.1 Part 1


>```
>$ cd docker/part1
>```

In this first part you are tasked to dockerize the python application. 

First create a file called **service.py** and copy paste the following:  
```
import hug
import random
import service

@hug.get()

def verify():
    return {
        'name': 'your_name',
        'school': 'your_school',
        'email': 'your_email',
        'id': random.randint(110,250)
    }

```

Then, create a file called **requirements.txt** to manage the requirements of our application: 
```
hug==2.6.1
gunicorn==19.8.1
pytest==3.7.0
```

In order to dockerize our application you need to create a **Dockerfile**. Inside this dockerfile you need to take under consideration the following: 

> - The code source should be copied in: `/usr/src/app`
> - To install the requirements RUN the following: `pip install --no-cache-dir -r requirements.txt`
> - Make sure to expose the application on port: `8080`
> - To execute the application, add the following instruction in your Dockerfile: `CMD ["gunicorn", "-b", "0.0.0.0:8080", "service:__hug_wsgi__"]`
