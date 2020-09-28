import requests
import json


class User:
    def __init__(self, data):
        self.data = data

    def get_name(self):
        return self.data["name"]

    def get_pis(self):
        return self.data["pis"]


class AFD:
    def __init__(self, afd, session):
        self.pis = int(afd[22:34])
        self.afd = afd
        self.session = session

    def get_original(self):
        return self.afd

    def get_parsed(self):
        string_date = self.afd[10:18]
        string_time = self.afd[18:22]
        fmt_string_date = f"{string_date[0:2]}/{string_date[2:4]}/{string_date[4:8]} {string_time[0:2]}:{string_time[2:5]}"

        return {
            "nsr": self.afd[0:9],
            "tipo_registro": self.afd[9],
            "pis": self.pis,
            "data": fmt_string_date,
        }


class Session:
    options = {
        "headers": {"Content-type": "application/json", "Accept": "text/plain",},
        "verify": False,
    }

    def __init__(self, user, password, host):
        self.host = host
        data = {"login": user, "password": password}
        response = requests.post(
            f"{host}/login.fcgi", data=json.dumps(data), **self.options
        )

        self.session = response.json()["session"]

    def post(self, url, data):
        return requests.post(
            f"{self.host}/{url}.fcgi",
            data=json.dumps(data),
            **self.options,
            params={"session": self.session},
        )

    def get_user_pis(self, list_pis):
        data = {"users_pis": list_pis}
        response = self.post("load_users", data)

        return_data = response.json()["users"]

        return return_data

    def get_afds(self, day, month, year, nsr):
        data = {
            "initial_date": {
                "day": day,
                "month": month,
                "year": year,
                "initial_nsr": nsr,
            }
        }

        response = self.post("get_afd", data)
        txt = response.text.split("\r\n")
        return_data = txt

        return return_data
