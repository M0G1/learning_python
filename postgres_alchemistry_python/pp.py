import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="M0g1_elf=MagHardworker2021", port=5432)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()
# Создаем базу данных
sql_create_database = cursor.execute('create database sqlalchemy_tuts')

# Закрываем соединение
cursor.close()
connection.close()
