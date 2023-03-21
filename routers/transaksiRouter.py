from uuid import uuid4
from fastapi import APIRouter, Response, status
from schemas.transaksi import Transaksi
from services import transaksiService
from exceptions.transaksiExceptions import RekeningNotFoundError
from validator import transaksiValidator

routes = APIRouter()

@routes.post('/tabung', status_code=200)
async def transaksiTabungHandler(data: Transaksi, response: Response):
    try:
        transaksiValidator.validate(data)
        transaksiService.addTransaksiTabung(data)

        saldo = transaksiService.getSaldo(data.no_rekening)

        return {
            'success': 'true',
            'message': 'transaksi tabung berhasil',
            'data': {
                'saldo': saldo
            }
        }
    except RekeningNotFoundError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        
        return {
            'success': 'false',
            'remark': 'Nomor rekening tidak ditemukan'
        }
    
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(e)
        return {
            'success': 'false',
            'message': 'terjadi server error, harap hubungi pengembang'
        }