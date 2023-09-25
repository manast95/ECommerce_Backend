#Basic method for JSON

def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "price": item["price"],
        "quantity": item["quantity"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

#Better method, used more frequently

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
