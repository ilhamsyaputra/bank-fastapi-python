from db.database import databaseConnect
from exceptions.transaksiExceptions import *

def validate(data):
    noRekening = data.no_rekening

    conn = databaseConnect()
    cursor = conn.cursor()

    cursor.execute(
        'select * from rekening where no_rekening = %s',
        (noRekening,)
    )

    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        raise RekeningNotFoundError