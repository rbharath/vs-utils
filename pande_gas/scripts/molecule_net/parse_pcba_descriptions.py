#!/usr/bin/env python
"""
Parse PCBA assay descriptions.
"""
import argparse

from pande_gas.utils.molecule_net import PcbaJsonParser, PcbaXmlParser


def parse_args(input_args=None):
    """
    Parse command-line arguments.

    Parameters
    ----------
    input_args : list, optional
        Input arguments. If not provided, defaults to sys.argv[1:].
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=1, nargs='+',
                        help='Input file(s) containing assay description(s).')
    parser.add_argument('-f', '--format', choices=['json', 'xml'],
                        default='json',
                        help='Input file format.')
    return parser.parse_args(input_args)


def main(filenames, input_format='json'):
    """
    Parse PCBA assay descriptions.

    Parameters
    ----------
    filenames : list
        Filenames containing assay descriptions.
    input_format : str, optional (default 'json')
        Input file format.
    """
    for filename in filenames:
        if input_format == 'json':
            parser = PcbaJsonParser(filename)
        elif input_format == 'xml':
            parser = PcbaXmlParser(filename)
        else:
            raise NotImplementedError(
                'Unrecognized input format "{}"'.format(input_format))

if __name__ == '__main__':
    args = parse_args()
    main(args.input, args.format)