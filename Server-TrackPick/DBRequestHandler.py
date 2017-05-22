import pymongo

# DB Requests for create, insert and update collection and documents

def CreateDatabase():
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)
    db = client['trackpick']
    collection = db['trackpick']

    if collection is not None:
        print(collection)
        print('Done')

