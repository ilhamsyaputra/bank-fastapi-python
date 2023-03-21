from db.database import databaseConnect
from exceptions.transaksiExceptions import *
from services import transaksiService

def validate(data):

    conn = databaseConnect()
    cursor = conn.cursor()

    cursor.execute(
        'select * from rekening where no_rekening = %s',
        (data,)
    )

    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        raise RekeningNotFoundError