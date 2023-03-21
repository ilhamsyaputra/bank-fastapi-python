from db.database import databaseConnect
from datetime import datetime

def addNasabah(data, id):
    nama = data.nama
    nik = data.nik
    no_hp = data.no_hp
    tanggal_registrasi = datetime.now()

    conn = databaseConnect()
    cursor = conn.cursor()

    cursor.execute(
        'insert into nasabah values (%s, %s, %s, %s, %s)',
        (id, nama, nik, no_hp, tanggal_registrasi)
    )

    conn.commit()
    conn.close()
