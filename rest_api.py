import json


class RestAPI:
    database = {}

    def __init__(self, database=None):
        users = {}

    def get(self, url, payload=None):
        return json.dumps({"users": []})

    def post(self, url, payload=None):
        if url == "/add":
            str_user = json.loads(payload)
            user = {"name": str_user["user"],
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                    }
            return json.dumps(user)
