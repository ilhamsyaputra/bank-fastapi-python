from db.database import databaseConnect
from exceptions.nasabahExceptions import *

def validate(data):
    nik = data.nik
    no_hp = data.no_hp

    conn = databaseConnect()
    cursor = conn.cursor()

    cursor.execute(
        'select * from nasabah where nik = %s or no_hp = %s',
        (nik, no_hp)
    )

    conn.commit()
    conn.close()

    if cursor.rowcount != 0:
        raise NasabahDuplicateError