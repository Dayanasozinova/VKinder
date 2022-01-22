
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import *
def inst_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password=f"{password_postgres}",
                                      host=f"{host}",
                                      port=f'{port}')
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()
        sql_create_database = f'create database {db_name}'
        cursor.execute(sql_create_database)
        create_user = f"create user {user_name_db} with password '{password_user_name}'"
        cursor.execute(create_user)
        owner_db = f"alter database {db_name} owner to {user_name_db}"
        cursor.execute(owner_db)
        print('База данных создана успешно.')


    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
