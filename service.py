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
