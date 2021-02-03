from whisker import Whisker

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def main(args):
    fibonacci(23)

    if 'actions' in args:
        cfg = Whisker('f8', args)
        cfg.run_next()

    return {
        'statusCode': 200
    }
