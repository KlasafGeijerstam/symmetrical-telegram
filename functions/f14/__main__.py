import json
import hashlib
from whisker import Whisker

def main(args):
    hashlib.pbkdf2_hmac('sha512', b'ServerlessAppPerfOpt', b'salt', 80000)

    if 'actions' in args:
        cfg = Whisker('f14', args)
        cfg.run_next()
    
    return {
        'statusCode': 200
    }
