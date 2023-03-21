import random
from datetime import datetime

SEED = datetime.timestamp(datetime.now())
BANKDIGIT = '787'


def generateNoRekening():
    random.seed(SEED)

    generatedRekening = BANKDIGIT + str(random.randrange(10**(7-1), 10**7))

    return generatedRekening
