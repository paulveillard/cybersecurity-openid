#!/usr/local/bin/python
import argparse, json

parser = argparse.ArgumentParser(description="Pretty Print JSON Input")
parser.add_argument("json", type=str, help="The JSON Object to pretty print.")
parser.add_argument("-n", "--no-indent", action="store_true", help="do not indent")
parser.add_argument("-l", "--indent-level", type=int, default=4, help="set indention level")
parser.add_argument("-s", "--sort-keys", action="store_true", help="sort JSON keys")
args = parser.parse_args()

if args.no_indent:
    indentlevel=None
else:
    indentlevel=args.indent_level

print ("Pretty Printing with %d" % args.indent_level)
parsed = json.loads(args.json)
print json.dumps(parsed,indent=indentlevel,sort_keys=args.sort_keys)
