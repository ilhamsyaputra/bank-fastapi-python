from db.database import databaseConnect
from exceptions.transaksiExceptions import *
from services import transaksiService

def validate(data):
    noRekening = data.no_rekening
    nominalTarik = data.nominal

    try:
        saldo = transaksiService.getSaldo(noRekening)
    except:
        raise RekeningNotFoundError

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
    
    if nominalTarik > saldo:
        raise LackSaldoError
    