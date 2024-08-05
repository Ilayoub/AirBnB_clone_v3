from importlib import import_module
import sys

try:
    mod_to_check = import_module(sys.argv[1])
    print(mod_to_check.__doc__)
except ImportError as e:
    print(e)
    pass
