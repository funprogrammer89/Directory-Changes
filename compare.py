from deepdiff import DeepDiff
import json
import hashfiles
import os
print("\033[95mEnter directory below to check for changes: \033[0m\n")
directory = input()
if os.path.exists(directory + "/files.json"):
    with open(directory + '/files.json') as json_file:
        data = json.load(json_file)
    filedic = dict()
    subdirs = [x[0] for x in os.walk(directory)]
    for x in subdirs:
        filedic = {**filedic, **hashfiles.gethashes(x + "/")}
    diff = DeepDiff(data, filedic,ignore_order=True,exclude_paths=directory+"/files.json")
    if len(diff) == 0:
        print("\nNo Changes")
    else:
        print()
        print("\033[94mChanges listed below : \n\033[0m")
        print(diff)
        print()
else:
    print("\033[94m\nNo \033[92m'files.json'\033[0m\033[94m file found in \033[93m'" + directory + "'\033[0m... "
                                                                                                   "\n\n\033[94mDid "
                                                                                                   "you use\033[0m "
                                                                                                   "\033[0m\033["
                                                                                                   "96m'setjson.py"
                                                                                                   "'\033[0m"
          "\033[94m first? \n\nDid your \033[0m\033[92m'files.json'\033[0m\033[94m file get deleted or moved?\033[0m")
