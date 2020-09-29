from .entities import User, AFD
import pandas as pd


def get_afds(session, day, month, year):
    afds_txt = session.get_afds(day, month, year, 1)
    afds = []

    for afd in afds_txt:
        try:
            obj = AFD(afd, session)
            afds.append(obj)
        except ValueError:
            continue

    return afds


def get_users_from_afds(session, afds):
    list_pis = map(lambda x: x.get_parsed()["pis"], afds)
    list_pis = list(set(list_pis))

    try:
        users = session.get_user_pis(list_pis)
    except KeyError:
        users = []

    return list(map(lambda x: User(x), users))


def transform_afds(afds, users):
    parsed = list(map(lambda x: x.get_parsed(), afds))
    final_data = []

    for user in users:
        afds_user = filter(lambda afd: afd["pis"] == int(user.get_pis()), parsed)

        for afd in afds_user:
            final_data.append({**afd, "funcionario": user.get_name()})

    return final_data


def to_csv(list_data, file_path):
    df = pd.DataFrame(list_data)
    df.to_csv(file_path)

    return
