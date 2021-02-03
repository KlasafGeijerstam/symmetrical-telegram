import whisker


def main(args):
    try:
        if 'entry_point' not in args['actions']:
            return {'error': 'no entry point for application'}

        config = whisker.Whisker('entry_point', args)
        return {"output": config.run_next()}
    except Exception as e:
        return {"error": str(e)}

    return args
