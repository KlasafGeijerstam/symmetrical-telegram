import time
from whisker import Whisker

def main(args):
    # Download a 10MB file from S3

    if 'actions' in args:
        cfg = Whisker('f16', args)
        cfg.run_next()

    return {
        'statusCode': 200
    }
