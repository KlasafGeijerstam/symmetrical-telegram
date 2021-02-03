import time
from whisker import Whisker, DOWNLOAD_PATH, UPLOAD_PATH
import requests

def main(args):

    # Download a 20MB file
    resp = requests.get(DOWNLOAD_PATH + '/20MB')
    with open('/tmp/20MB', 'wb') as f:
        f.write(resp.content)
    time.sleep(0.1)

    # Upload a 20MB file
    with open('/tmp/20MB', 'rb') as f:
        files = { 'data': f }
        requests.post(UPLOAD_PATH, files=files)

    if 'actions' in args:
        cfg = Whisker('f12', args)
        cfg.run_next()

    return {
        'statusCode': 200
    }
