from whisker import Whisker

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def main(args):
    fibonacci(28)
    
    if 'actions' in args:
        cfg = Whisker('f3', args)
        cfg.run_next()


    return {
        'statusCode': 200
    }
