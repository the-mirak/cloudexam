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
    - writer
    - reader
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

Finally, build then push the image to your dockerhub repository under the following name: `reader:1.0`


### 1.2 Part 2

>```
>$ cd docker/part2
>```

In this second part, we are going to make our display dynamique through environment variables.
To do so, makes sure that your **serivce.py** file matches the following: 
```
import hug
import random
import service
import os

@hug.get()

def verify():
    name = os.environ['NAME']
    school = os.environ['SCHOOL']
    email = os.environ['EMAIL']
    return {
        'name': name,
        'school': school,
        'email': email,
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
> - Use the following environments variables in your Dockerfile `NAME="df_your_name"`, `SCHOOL="df_your_school"`, `EMAIL="df_your_email"` 
> - The code source should be copied in: `/usr/src/app`
> - To install the requirements RUN the following: `pip install --no-cache-dir -r requirements.txt`
> - Make sure to expose the application on port: `8080`
> - To execute the application, add the following instruction in your Dockerfile: `CMD ["gunicorn", "-b", "0.0.0.0:8080", "service:__hug_wsgi__"]`

Finally, build then push the image to your dockerhub repository under the following name: `reader:2.0`


### 1.3 Part 3

>```
>$ cd docker/part3
>```

In this third part, we are going to break our application into 3 services. 
- Database service
  - `docker run --name mydbserver -e MYSQL_ROOT_PASSWORD=mypassword -d mysql`
- Writer service
- Reader service

#### 1.3.1 Writer service

>```
>$ cd docker/part3/writer
>```

First, let us create the writer service which is responsible to writing our information in the database. 
To do so, create a file called **writer.py** and copy paste the following: 
```
import mysql.connector
import os 

name = os.environ['NAME']
school = os.environ['SCHOOL']
email = os.environ['EMAIL']

mydb = mysql.connector.connect(
  host="mydbserver",
  user="root",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("USE mydatabase")


mycursor.execute("CREATE TABLE exam (name VARCHAR(255), school VARCHAR(255), email VARCHAR(255))")

sql = "INSERT INTO exam (name, school, email) VALUES (%s, %s, %s)"
val = (name, school, email)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

```

Then, create a file called **requirements.txt** to manage the requirements of our application: 
```
mysql-connector-python==8.0.27
mysql-connector-python-rf==2.2.2
```

In order to dockerize our application you need to create a **Dockerfile**. Inside this dockerfile you need to take under consideration the following: 
> - Use the following environments variables in your Dockerfile `NAME="ms-your_name"`, `SCHOOL="ms-your_school"`, `EMAIL="ms-your_email"` 
> - To run the application add the following instruction in your Dockerfile `CMD [ "python", "./writer.py" ]`

Finally, build then push the image to your dockerhub repository under the following name: `writer:3.0`


#### 1.3.2 Reader service

>```
>$ cd docker/part3/reader
>```

Secondly, let us create the reader service which is responsible to read our information from the database and display them. 
To do so, create a file called **service.py** and copy paste the following: 
```
import hug
import random
import service
import mysql.connector

mydb = mysql.connector.connect(
  host="mydbserver",
  user="root",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM exam")
name = mycursor.fetchone()

mycursor.execute("SELECT school FROM exam")
school = mycursor.fetchone()

mycursor.execute("SELECT email FROM exam")
email = mycursor.fetchone()

@hug.get()

def verify():
    return {
        'name': name,
        'school': school,
        'email': email,
        'id': random.randint(110,250)
    }
```

Then, create a file called **requirements.txt** to manage the requirements of our application: 
```
hug==2.6.1
gunicorn==19.8.1
pytest==3.7.0
mysql-connector-python==8.0.27
mysql-connector-python-rf==2.2.2
```

In order to dockerize our application you need to create a **Dockerfile**. Inside this dockerfile you need to take under consideration the following: 
> - The code source should be copied in: `/usr/src/app`
> - To install the requirements RUN the following: `pip install --no-cache-dir -r requirements.txt`
> - Make sure to expose the application on port: `8080`
> - To execute the application, add the following instruction in your Dockerfile: `CMD ["gunicorn", "-b", "0.0.0.0:8080", "service:__hug_wsgi__"]`
 
Finally, build then push the image to your dockerhub repository under the following name: `reader:3.0`


### 1.4 Part 4:

>```
>$ cd docker/
>$ cp -r docker/part3 docker/part4
>$ cd docker/part4
>```

In this final part, we are going to put our application in a docker compose file. 
To do so, write a **docker-compose.yaml** file by taking under the consideration the following instructions: 

- Create three services: 
  - reader
    - Build the image in the docker compose file
    - Name the container **reader**
    - The reader service depends on the mydbserver service *(find the healthcheck script for mysql in the healthcheck folder)*
    - expose and publish the application on port 8080 
    - Connect the service to the "myappnetwork" network
  - writer
    - Build the image in the docker compose file
    - Name the container **wirter**
    - The writer service depends on the mydbserve servuce *(find the healthcheck script for mysql in the healthcheck folder)*
    - The writer service depends on the reader service being started 
    - Connect the service to the "myappnetwork" network
  - mydbserver
    - use the latest mysql 
    - Name the container **mydbserver**
    - Declare the environment variable MYSQL_ROOT_PASSWORD with the following value "mypassword"
    - expose the application on port 3306  
    - Connect the service to the "myappnetwork" network


## 2. Section 2 
 
In this second section we will take our python application to the kubernetes environment and deploy it. 
For this section create the following directory: 
- kubernetes

>```
>$ cd kubernetes
>```

In order to deploy our application in kubernetes, we will need to create the following resources: 
- Pods: 
  - mydbserver pod
    - Declare the port used by the container 
```yaml
    - containerPort: 3306
```
    - Use the following image name `mysql`
    - Declare the following environment variable
```yaml
    - name: MYSQL_ROOT_PASSWORD
      value: mypassword
```
  - writer pod
    - Use the image `writer:3.0` you pushed in 1.3.1
    - Declare the following environment variable
```yaml
    - name: NAME
      value: k8s-yourname
    - name: EMAIL
      value: k8s-your_email
    - name: SCHOOL
      value: k8s-your_school
```
  - reader
    - Use the image `reader:3.0` you pushed in 1.3.2
    - Declare the port used by the container 
```yaml
    - containerPort: 8080
```

- Services: 
  - mydbserver service
    - This service needs to be exposed internally 
  - reader service
    - This service needs to be exposed externally 
 
<br>

Congratulations you have reached the end!

<br>

_Cloud Computing-Mundiapolis, 2021/2022_
