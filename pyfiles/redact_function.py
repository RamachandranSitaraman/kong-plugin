#!/usr/bin/env python3

import sys
import os
import kong_pdk.pdk.kong as kong
import json

def transform1(body):
        resp = json.loads(body)
        resp['text'] = 'test'
        return json.dumps(resp)

def concatenate_string(input_string):
    return input_string + input_string

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./concat_string.py <string>")
        sys.exit(1)

    input_string = sys.argv[1]
    result = transform1(input_string)
    return(result)
