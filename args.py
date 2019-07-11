
# args.py

"""
    parse arguments in the traditional unix way:
    -f --flag[=WORD] positional
    returns a list of arguments and key-value pairs
"""


def flag(*flags):
    """ a decortator that registers a handler function with an option flag or flags """
    def _register_flag(flag_func):
        for f in flags:
            flag.handlers[f] = flag_func
    return _register_flag
flag.handlers = {}

def _handle_flags(flags):
    for f in flags:
        try:
            flag.handlers[f]()
        except Exception as e:
            print('No handler for : ', e)
flag.handle = _handle_flags

def pair(*keys, convert=lambda x: x, required=True):
    """ a decortator that registers a handler function with an option pair or pairs
        accepts a variable number of arguments for keys to match and a convert function"""
    # allow the convert function to be included without the keyword
    if hasattr(keys[-1], '__call__'): convert = keys[-1]
    # allow the required function to be included without the keyword
    if isinstance(keys[-1], bool): required = keys[-1]

    def _register_pair(pair_func):

        def h(val):
            try:
                val = convert(val)
            except ValueError as E:
                raise ValueError('Could not convert argument: ' + E)

            return pair_func(val)

        for key in keys:
            pair.handlers[key] = h
    return _register_pair
pair.handlers = {}

def _handle_pairs(pairs):
    for key, val in pairs.items():
        try:
            pair.handlers[key](val)
        except Exception as e:
            print('No handler for : ', e)

pair.handle = _handle_pairs

def parse(args):
    """ parses a list of argument strings and returns a tuple of the form ([flags], [pairs], [args]) """
    pos = []
    flags = []
    pairs = {}

    for arg in args:

        if arg.startswith('--'):
            arg = arg[2:]
            if '=' in arg:
                k, v = arg.split('=')
                pairs[k]=v
                continue
            flags.append(arg)
            continue

        if arg.startswith('-'):
            for c in arg[1:]:
                flags.append(c)
            continue

        pos.append(arg)

    return flags, pairs, pos

    
if __name__=='__main__':
    import sys
    def container():
        @flag('force', 'f', True)
        def testfunc():
            print('called testfunc --force')

        @pair('commit-message', lambda s: s.split())
        def cmlist(messages):
            print('cmlist : ', messages)

        @pair('commit-message')
        def cm(message):
            print('cm : ', message)

        @pair('num-runs', 'runs', 'nruns', int, required=True)
        def num_runs(n):
            print('num-runs : ', n, 'n squared : ', n**2)
    container()

    print(parse(sys.argv))
    flags, pairs, pos = parse(sys.argv)
    flag.handle(flags)
    pair.handle(pairs)
    

