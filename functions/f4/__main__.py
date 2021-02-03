import time
import requests
from whisker import Whisker, DOWNLOAD_PATH, UPLOAD_PATH

def main(args):
    # Download a 25MB file
    resp = requests.get(DOWNLOAD_PATH + '/25MB')
    with open('/tmp/25MB', 'wb') as f:
        f.write(resp.content)
    time.sleep(0.1)

    # Upload a 25MB file
    with open('/tmp/25MB', 'rb') as f:
        files = { 'data': f }
        requests.post(UPLOAD_PATH, files=files)

    if 'actions' in args:
        cfg = Whisker('f4', args)
        cfg.run_next()

    return {
        'statusCode': 200
    }
