#!/usr/local/bin/python2.7
from jose import jwt
import argparse, json

parser = argparse.ArgumentParser(description="Decode a JWT")
parser.add_argument("jwt", type=str, help="The JWT to decode.")
parser.add_argument("-i", "--indent", action="store_true", help="pretty print JSON")
parser.add_argument("-s", "--sort-keys", action="store_true", help="sort JSON keys")
args = parser.parse_args()

if args.indent:
    indentlevel=4
else:
    indentlevel=None

header = jwt.get_unverified_header(args.jwt)
body = jwt.get_unverified_claims(args.jwt)

print json.dumps(header,indent=indentlevel,sort_keys=args.sort_keys)
print (".")
print json.dumps(body,indent=indentlevel,sort_keys=args.sort_keys)
