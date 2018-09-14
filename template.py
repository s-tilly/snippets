#!/usr/bin/env python3

# To use it,
# > virtualenv template
# > source template/bin/activate
# > python template.py -h

from configparser import ConfigParser
from pprint import pprint
import argparse
import io
import os
import sys

import jinja2
from jinja2 import Template
from jinja2 import Environment


def construct_vars(config):
    """Construct jinja2 keys from configParser

    Don't care about sections. So don't duplicate var name.
    """
    c = ConfigParser()
    c.readfp(open(config))
    keys = []
    for s in c.sections():
        keys += c.items(s)
    return dict(keys)

description="""Simple Jinja2 template executor."""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=description)
    parser.add_argument('-c', '--config', required=True, default=None, action='store', help="Configuration file to use")
    parser.add_argument('-i', '--input', required=True, default=False, action='store', help="Input template")
    parser.add_argument('-o', '--output', required=False, default="-", action='store', help="Output file, to stdout if nothing or '-'")
    args = parser.parse_args()

    keys = construct_vars(args.config)
    env = Environment(loader=jinja2.FileSystemLoader(['.', '/']), undefined=jinja2.StrictUndefined)

    #with io.open(args.input, mode='r', encoding='utf-8') as f:
    #    template = Template(f.read())
    template = env.get_template(os.path.abspath(args.input))
    result = template.render(keys)
    if args.output == '-':
        sys.stdout.write(result)
    else:
        with io.open(args.output, mode='w', newline='\n', encoding='utf-8') as f:
            f.write(result)
