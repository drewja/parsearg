# args.py

"""
    parse arguments in the traditional unix way:
    -f --flag[=WORD] positional
    returns a list of arguments and key-value pairs
"""

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

    return pos, flags, pairs
