from db.database import databaseConnect
from datetime import datetime

def getRekeningId(no_rekening):
    conn = databaseConnect()
    cursor = conn.cursor()

    cursor.execute(
        'select id from rekening where no_rekening = %s',
        (no_rekening,)
    )

    return cursor.fetchone()[0]

def getSaldo(no_rekening):
    conn = databaseConnect()
    cursor = conn.cursor()

    cursor.execute(
        'select saldo from rekening where no_rekening = %s',
        (no_rekening,)
    )

    return cursor.fetchone()[0]

def updateSaldo(no_rekening, saldo):
    conn = databaseConnect()
    cursor = conn.cursor()

    cursor.execute(
        'update rekening set saldo = %s where no_rekening = %s',
        (saldo, no_rekening)
    )
    conn.commit()

def addTransaksiTabung(data):
    rekening_id = getRekeningId(data.no_rekening)
    waktu_transaksi = datetime.now()
    saldo = getSaldo(data.no_rekening)
    nominal = data.nominal
    updatedSaldo = saldo + nominal


    conn = databaseConnect()
    cursor = conn.cursor()

    cursor.execute(
        'insert into transaksi(rekening_id,  nominal, tipe, waktu) values (%s, %s, %s, %s)',
        (rekening_id, nominal, 'C', waktu_transaksi)
    )

    updateSaldo(data.no_rekening, updatedSaldo)

    conn.commit()
    conn.close()