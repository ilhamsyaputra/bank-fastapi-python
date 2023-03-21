from fastapi import APIRouter, Response, status
from services import transaksiService
from exceptions.transaksiExceptions import RekeningNotFoundError
from validator import mutasiValidator

routes = APIRouter()

@routes.get('/mutasi/{no_rekening}', status_code=200)
async def getMutasiHandler(no_rekening, response: Response):
    try:
        mutasiValidator.validate(no_rekening)
        data = transaksiService.getMutasiByRekening(no_rekening)
        
        out = []

        for i in data:
            dictData = {
                'waktu': i[4],
                'kode_transaksi': i[3],
                'nominal': i[2]
            }
            
            out.append(dictData)

        return {
            'success': 'true',
            'message': 'sukses mendapatkan mutasi',
            'data': out
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