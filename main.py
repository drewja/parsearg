# main.py

"""
    parse arguments in the traditional unix way:
    -f --flag[=WORD] positional
    returns a list of arguments and key-value pairs
"""
from typing import Sequence, Tuple, List, Dict

def parse(args: Sequence[str]) -> Tuple[list, list, dict]:
    """ 
        parses a list of argument strings and returns a tuple of the form 
        ([args], [flags], {flag pairs})
    """
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

if __name__ == '__main__':
    import sys
    print(parse(sys.argv))