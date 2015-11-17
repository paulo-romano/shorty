db = list()

def add_url(goto):
    db.append(goto)
    return db.index(goto)

def get_url(target):
    return db[target]
