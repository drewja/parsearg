"""
    parse arguments in the traditional unix way:
    -f --flag --flag[=WORD] positional
"""
from typing import Sequence, Tuple, List, Dict

def parse(arguments: Sequence[str]) -> Tuple[list, list, dict]:
    """ 
        Parses an iterable of argument strings and returns a tuple of arguments,
        flags, and key-value pairs. ([args], [flags], {flag pairs})
    """
    pos = []
    flags = []  
    pairs = {}

    for arg in arguments:

        if arg.startswith('--'):
            arg = arg[2:]
            if '=' in arg:
                k, v = arg.split('=', 1)
                pairs[k] = v
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