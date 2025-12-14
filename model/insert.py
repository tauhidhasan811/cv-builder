from component.config.db_config import GetDBConnection

def insert_one(data, cl_name):
    db_name = GetDBConnection()
    collection_name = db_name[cl_name]
    response = collection_name.insert_one(data)
    id = str(response.inserted_id)
    return id

