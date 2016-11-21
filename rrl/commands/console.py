#!/usr/bin/env python
"""
provides the console commands
"""
import sys
import argparse
from rrl.interpreter import run_script


def rrl():
    """
    rrl console command.
    """

    class MyParser(argparse.ArgumentParser):
        """
        Custom argument parser for printing help message in case of an error.
        """
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    parser = MyParser(description='textX checker and visualizer')
    parser.add_argument('cmd', help='Command - "check" or "run"')
    parser.add_argument('script', help='RRL script file name', nargs='?')

    args = parser.parse_args()

    if args.cmd not in ['run', 'check']:
        print("Unknown command {}. Command must be one of"
              " 'run', 'check'.".format(args.cmd))
        sys.exit(1)

    run_script(args.script, debug=False)
