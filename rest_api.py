import json


class RestAPI:

    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if payload == None:
            return {"users": []}
        results = []
        for u in self.database["users"]:
            for p in json.loads(payload)["users"]:
                if((u["name"]) ==p):
                    results.append(u)

        return json.dumps(results)

    def post(self, url, payload=None):
        if url == "/add":
            str_user = json.loads(payload)
            user = {"name": str_user["user"],
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                    }
            self.database[str_user["user"]] = user
            return json.dumps(user)
