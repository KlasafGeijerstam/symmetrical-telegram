import os
from whisker import Whisker

def main(args):
    path = '/tmp/1MB'
    file_indicator=os.path.isfile(path)
    if file_indicator:
        os.remove(path)
    for i in range(58):
        f = open(path, 'wb')
        f.write(os.urandom(1048576))
        f.flush() 
        os.fsync(f.fileno()) 
        f.close() 

    if 'actions' in args:
        cfg = Whisker('f11', args)
        cfg.run_next()
    
    return {
        'statusCode': 200
    }
