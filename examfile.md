

# ipsum lorem


## ipsum lorem

 
ipsum lorem **ipsum lorem** ipsum lorem.
 

ipsum lorem
- ipsum loremE
- ipsum lorem
- ipsum lorem


### 1. ipsum lorem

ipsum lorem

Part 1: 

First app 

service.py

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



requirements.txt
```
hug==2.6.1
gunicorn==19.8.1
pytest==3.7.0
```


The code source should be copied at `/usr/src/app`
To install the requirements run the following `pip install --no-cache-dir -r requirements.txt`

Make sure to expose the application on the following port `8080`

To run the application add the following instruction in your Dockerfile `CMD ["gunicorn", "-b", "0.0.0.0:8080", "service:__hug_wsgi__"]
`


##############################

Part 2: 


serivce.py
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

requirements.txt
```
hug==2.6.1
gunicorn==19.8.1
pytest==3.7.0
```


use the following environments variables in your Dockerfile `NAME="df_your_name"`, `SCHOOL="df_your_school"`, `EMAIL="df_your_email"`  


#################

Part 3:

writer.py 
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

requirements.txt
```
mysql-connector-python==8.0.27
mysql-connector-python-rf==2.2.2
```
use the following environments variables in your Dockerfile `NAME="ms_your_name"`, `SCHOOL="ms_your_school"`, `EMAIL="ms_your_email"` 

To run the application add the following instruction in your Dockerfile `CMD [ "python", "./writer.py" ]`



service.py
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


requirements.txt
```
hug==2.6.1
gunicorn==19.8.1
pytest==3.7.0
mysql-connector-python==8.0.27
mysql-connector-python-rf==2.2.2
```



part 4:

write a docker compose file abiding by the following instruction: 

Create three services (make sure to name your containers): 
  - reader
    - build the image in the docker compose file
    - The reader depends on the mydbserver (find the healthcheck script for mysql in the healthcheck folder)
    - expose and publish the application on 8080 port 
  - writer
    - build the image in the docker compose file
    - The writer depends on the mydbserver (find the healthcheck script for mysql in the healthcheck folder)
    - The writer depends on the reader being just started 
  - mydbserver
    - use the latest mysql image
    - Declare the environment variable MYSQL_ROOT_PASSWORD with the following value mypassword
    - expose the application on 3306 port 

 
part 5:

Push the images created in part 3 to your docker hub under the following naming convention:
  - ` reader:3.0 `
  - ` writer:3.0 `


Create the following pods: 
  - mydbserver pod
    - Use the following image name `mysql`
    - Declare the port used by the container 
```yaml
    - containerPort: 3306
```    
    - Declare the following environment variable
```yaml
    - name: MYSQL_ROOT_PASSWORD
      value: mypassword
```
  - writer pod
    - Use the image `writer:3.0` pushed by you
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
    - Use the image `reader:3.0` pushed by you
    - Declare the port used by the container 
```yaml
    - containerPort: 8080
```

Create the following service: 
  - mydbserver service
    - This service needs to be exposed internally 
  - reader service
    - This service needs to be exposed externally 




 
ipsum lorem:

> N.B. The `; ipsum lorem` ipsum lorem `ipsum lorem` oipsum lorem

 
 
<br>

Congratulations ipsum lorem!

<br>

_ipsum lorem_
