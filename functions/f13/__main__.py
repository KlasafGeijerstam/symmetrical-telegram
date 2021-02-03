from whisker import Whisker

def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

def main(args):
    factorial(30000)
    
    if 'actions' in args:
        cfg = Whisker('f13', args)
        cfg.run_next()

    return {
        'statusCode': 200
    }
