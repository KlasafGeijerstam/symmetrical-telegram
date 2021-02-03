import time
from whisker import Whisker

def main(args):
    # Download a 25MB file from S3
    time.sleep(0.1)
    #Delete the file on S3
    time.sleep(0.1)
    # Upload a 25MB file to S3

    if 'actions' in args:
        cfg = Whisker('f4', args)
        cfg.run_next()

    return {
        'statusCode': 200
    }
