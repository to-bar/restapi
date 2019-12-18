import json


class RestAPI:
    database = {"users": []}

    def __init__(self, database=None):
        RestAPI.database = database

    def get(self, url, payload=None):
        if payload == None:
            return json.dumps({"users": []})
        results = []
        for u in self.database["users"]:
            for p in json.loads(payload)["users"]:
                if((u["name"]) ==p):
                    results.append(u)

        return json.dumps({"users": results})

    @staticmethod
    def get_user_data(user_name):
        return RestAPI.database['users'][RestAPI.get_user_index(user_name)]

    @staticmethod
    def get_user_index(user_name):
        return next(i for i, item in enumerate(RestAPI.database['users']) if item["name"] == user_name)

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
        if url == "/iou":
            payload = json.loads(payload)
            lender = RestAPI.get_user_data(payload['lender'])
            borrower = RestAPI.get_user_data(payload['borrower'])
            print(RestAPI.database['users'][RestAPI.get_user_index(lender['name'])]['owed_by'])

            RestAPI.database['users'][RestAPI.get_user_index(lender['name'])]['owed_by'][borrower['name']] = payload['amount']
            RestAPI.database['users'][RestAPI.get_user_index(lender['name'])]['balance'] = payload['amount']
            RestAPI.database['users'][RestAPI.get_user_index(borrower['name'])]['owes'][lender['name']] = payload['amount']
            RestAPI.database['users'][RestAPI.get_user_index(borrower['name'])]['balance'] = -payload['amount']
            return json.dumps({ "users": sorted([lender, borrower], key=lambda x: x['name']) })




