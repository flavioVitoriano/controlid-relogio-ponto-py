from controlidpy.entities import Session
from controlidpy.functions import get_afds, get_users_from_afds, transform_afds, to_csv


session = Session("admin", "admin", "https://192.168.0.98")
afds = get_afds(session, 10, 4, 2020)
users = get_users_from_afds(session, afds)
final = transform_afds(session, afds, users)

to_csv(final, "csv_example.csv")
