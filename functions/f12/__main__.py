import time
from whisker import Whisker

def main(args):
    # Download a 20MB file from S3
    time.sleep(0.1)
    #Delete the file on S3
    time.sleep(0.1)
    # Upload a 20MB file to S3

    if 'actions' in args:
        cfg = Whisker('f12', args)
        cfg.run_next()

    return {
        'statusCode': 200
    }
