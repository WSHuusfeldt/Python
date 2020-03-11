import sys
from urllib.parse import urlparse
import logging
import ex
from pprint import pprint
import getopt


log_fmt = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_fmt)


def usage():
    return 'Usage : CLI_ex.py csv_file_path'


def run(arguments):
    """Fandt ikke ud af hvordan jeg lavede --file file_name"""
    try:
        opts, args = getopt.getopt(arguments, "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    output = None
    for option, argument in opts:
        print(option)
        
        if option in ("-h", "--help"):
            print(usage())
            sys.exit()
        else:
            assert False, "unhandled option"
    
    
    pprint(ex.read_csv(args[0]))
    sys.exit()
    


if __name__ == '__main__':
    # Call me from the CLI for example with:
    # python your_script.py arg_1 [arg_2 ...]
    run(sys.argv[1:])