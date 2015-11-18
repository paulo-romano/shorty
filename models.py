import random
import string

db = dict()

def create_target():
    newtarget = ''
    for i in range(4):
        newtarget += random.choice(string.ascii_lowercase)
    if db.get(newtarget):
        newtarget = create_target()
    return newtarget

def add_url(goto):
    target = create_target()
    db[target] = goto
    return target

def get_url(target):
    return db.get(target)
