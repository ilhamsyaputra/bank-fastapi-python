import os
import psycopg2

from dotenv import load_dotenv
import psycopg2.extras



def databaseConnect():
    load_dotenv(override=True)

    psycopg2.extras.register_uuid()

    return psycopg2.connect(
        database = os.getenv('DATABASE'),
        host = os.getenv('HOST'),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD'),
        port = os.getenv('PORT')
    )