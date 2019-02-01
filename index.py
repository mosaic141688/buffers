# Copyright (c) Alex Ellis 2017. All rights reserved.
# Copyright (c) OpenFaaS Author(s) 2018. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import sys
from function import handler
import json
import urllib

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line

    return buf

def check_params(params):
    if not params.isalnum:
        raise "Param is not a number"
    pass

def retrieve_remote_files(params):
    params = json.loads(params)
    print(params)
    subject = params['subject']
    for key in subject.keys():
        if subject[key].startswith("http://") or subject[key].startswith("https://"):
            # fetch web resourse
            subject[payload][key] = json.loads(urllib.urlopen(subject[key]).read())
    return params
    
def main(): 
    if __name__ == "__main__":
        params = get_stdin()
        check_params(params)

        retrieve_remote_files(params)

        print(params)
      #  try:
       #     handler.handle(params)
       #     pass
      #  except Exception as e:
       #     print(e)

main() 