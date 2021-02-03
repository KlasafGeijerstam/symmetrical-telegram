import time
from whisker import Whisker, DOWNLOAD_PATH, UPLOAD_PATH
import requests

def main(args):
    # Download a 10MB file
    resp = requests.get(DOWNLOAD_PATH + '/10MB')
    with open('/tmp/10MB', 'wb') as f:
        f.write(resp.content)
    time.sleep(0.1)


    if 'actions' in args:
        cfg = Whisker('f16', args)
        cfg.run_next()

    return {
        'statusCode': 200
    }
