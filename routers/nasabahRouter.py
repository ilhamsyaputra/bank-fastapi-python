from uuid import uuid4
from fastapi import APIRouter, Response, status
from schemas.nasabah import Nasabah
from services import nasabahService, rekeningService
from validator import nasabahValidator
from exceptions.nasabahExceptions import *
from utils.generateRekening import generateNoRekening

routes = APIRouter()

@routes.post('/daftar', status_code=200)
async def addNasabahHandler(data: Nasabah, response: Response):
    try:
        id = uuid4()
        no_rekening = generateNoRekening()


        nasabahValidator.validate(data)
        nasabahService.addNasabah(data, id)
        rekeningService.addRekening(id, no_rekening)

        return {
            f'success': 'true',
            'message': 'nasabah baru berhasil ditambahkan',
            'data': {
                'no_rekening': no_rekening
            }
        }
    
    except NasabahDuplicateError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'success': 'false',
            'remark': 'NIK atau No HP sudah terdaftar, gagal membuat akun baru'
        }
    
    except Exception as e:
        print(e)
        return {
            'success': 'false',
            'message': 'terjadi error, harap hubungi pengembang'
        }