from db.database import databaseConnect

def addRekening(nasabahId, no_rekening):
    conn = databaseConnect()
    cursor = conn.cursor()


    cursor.execute(
        'insert into rekening(nasabah_id, no_rekening) values (%s, %s)',
        (nasabahId, no_rekening)
    )

    conn.commit()
    conn.close()