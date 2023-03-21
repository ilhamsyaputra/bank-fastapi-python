from fastapi import APIRouter, Response, status
from services import transaksiService
from validator import saldoValidator
from exceptions.transaksiExceptions import RekeningNotFoundError

routes = APIRouter()

@routes.get('/saldo/{no_rekening}', status_code=200)
async def getSaldoHandler(no_rekening, response: Response):
    try:
        saldoValidator.validate(no_rekening)
        saldo = transaksiService.getSaldo(no_rekening)

        return {
            'success': 'true',
            'message': 'sukses mendapatkan saldo',
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