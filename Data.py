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


# registration(3, 445656, 'Артур', 'Гаязов', 2, '1999', '60')

