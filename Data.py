import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://artur2:ybvajhn@localhost:5432/vkinder')
engine
connection = engine.connect()
connection
#
# def registration(id, id_vk, first_name, last_name, sex=None, bdate=None, city=None,):
#     connection.execute(f"""INSERT INTO users (id, id_vk, first_name, last_name, sex, bdate, city, home_town)
#             VALUES ({id}, {id_vk}, {first_name}, {last_name}, {sex}, {bdate}, {city});""")
#
# registration(1, 445656, 'Артур', 'Гаязов', 2, '1999', '60')
id = 2
id_vk = 9313245
first_name = 'Бен'
last_name = 'ЖЖ'
sex = 2
bdate = 1999
city = 3
connection.execute(f"""INSERT INTO users (id, id_vk, first_name, last_name, sex, bdate, city)
            VALUES ({id}, {id_vk}, {first_name}, {last_name}, {sex}, {bdate}, {city});""")