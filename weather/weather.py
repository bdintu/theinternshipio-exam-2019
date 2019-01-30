import os
import argparse
import json

from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring


def arg_parse():
    parser = argparse.ArgumentParser(description='XML to JSON Example')
    parser.add_argument('-f', '--file',
            help='XML input fiename')
    parser.add_argument('-o', '--output',
            help='JSON output filename')

    args = parser.parse_args()
    xml_in_path = args.file
    json_out_path = args.output

    if not json_out_path:
        base = os.path.basename(xml_in_path)
        filename, ext = os.path.splitext(base)
        json_out_path = filename + '.json'

    return xml_in_path, json_out_path

def read(xml_in_path):
    with open(xml_in_path) as xml_in:
        xml_data = xml_in.read()
    return xml_data

def write(data, json_out_path=''):
    with open(json_out_path, 'w') as json_out:
        json.dump(data, json_out, indent='\t')

def covent(xml_data):
    element_tree = fromstring(xml_data)
    badgerfish_data = bf.data(element_tree)
    return badgerfish_data

def main():
    xml_in_path, json_out_path = arg_parse()
    xml_data = read(xml_in_path)
    badgerfish_data = covent(xml_data) 
    write(badgerfish_data, json_out_path)


if __name__ == '__main__':
    main()
