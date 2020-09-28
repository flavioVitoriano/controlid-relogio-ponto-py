#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
import requests
import json


# In[ ]:


class User:
    def __init__(self, data):
        self.data = data
    
    def get_name(self):
        return self.data['name']
    
    def get_pis(self):
        return self.data['pis']
        


# In[ ]:


class AFD:
    def __init__(self, afd, session):
        self.afd = afd;
        self.session = session;
        
    def get_original(self):
        return self.afd

    def get_parsed(self):
        string_date = self.afd[10:18]
        string_time = self.afd[18:22]
        pis = int(self.afd[22:34])
        fmt_string_date = f"{string_date[0:2]}/{string_date[2:4]}/{string_date[4:8]} {string_time[0:2]}:{string_time[2:5]}"

        return {
        "nsr" : self.afd[0:9],
        "tipo_registro" : self.afd[9],
        "pis" : int(self.afd[22:34]),
        "data" : fmt_string_date,
        }
        


# In[ ]:


class Session:
    options = {
        'headers': {
            'Content-type': 'application/json',
            'Accept': 'text/plain',
        },
        'verify':False,
    }
    
    def __init__(self, user, password, host):
        self.host = host
        data = {
            "login": user,
            "password": password
        }
        response = requests.post(f"{host}/login.fcgi", data=json.dumps(data), **self.options)
        
        self.session = response.json()['session']
    
    def post(self, url ,data):
        return requests.post(f"{self.host}/{url}.fcgi", data=json.dumps(data), **self.options, params={"session": self.session})
    
    def get_user_pis(self, list_pis):
        data = {
            "users_pis": [list_pis]
        }
        response = self.post("load_users", data)

        return_data = response.json()['users']
        
        return return_data
    
    
    def get_afds(self, day, month, year, nsr):
        data = {
            "initial_date": {
                "day": day,
                "month": month,
                "year": year,
                "initial_nsr": nsr
            }
        }
        
        response = self.post("get_afd", data)
        txt = response.text.split('\r\n')
        return_data = txt
        
        return return_data
    


# In[ ]:


def get_afds(session, day, month, year):
    afds_txt = session.get_afds(day, month ,year, 1)
    afds = []
    
    for afd in afds_txt:
        try:
            afds.append(AFD(afd, session))
            print(AFD(afd, session).get_parsed())
            
        except ValueError:
            continue

    return afds


def get_users_from_afds(session, afds):
    list_pis = map(lambda x: x['pis'], afds)
    list_pis = set(list_pis)
    
    return session.get_user_pis(list_pis)
    


# In[ ]:


session = Session("admin", "admin", "https://192.168.0.98")
afds = get_afds(session)


# In[ ]:





# In[ ]:




