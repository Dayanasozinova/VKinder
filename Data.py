import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://artur2:ybvajhn@localhost:5432/vkinder')
engine
connection = engine.connect()
connection



def registration(id_vk, first_name, last_name, sex=None, bdate=None, city=None, home_town=None):
    if id_vk != connection.execute("""SELECT id_vk FROM users;""").fetchall()[0][0]:
        connection.execute(f"""INSERT INTO users (id_vk, first_name, last_name, sex, bdate, city, home_town)
                VALUES ({id_vk}, '{first_name}', '{last_name}', {sex}, {bdate}, {city}, '{home_town}');""")
    else:
        pass

def users_search_db(id_vk, json):
    connection.execute(f"""INSERT INTO users_search(user_id, usdb) 
                    VALUES ('{id_vk}','{json}');""")

def usdb (user_id):
    usid = []
    cursor = connection.execute(f"""SELECT usdb FROM users_search WHERE user_id = {user_id};""")
    for row in cursor:
        usid.append(row['usdb'])
    return usid

def iddb():
    iddb = []
    for row in connection.execute("""SELECT user_id FROM users_search;"""):
        iddb.append(row['user_id'])
    return iddb
