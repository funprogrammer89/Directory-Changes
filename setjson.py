import hashfiles
import os
import json
filedic = dict()
# walk through directory and all subdirectories
print("\033[95mEnter a directory below where a \033[96m'files.json'\033[0m\033[95m file will be saved that will store"
      "the state of the directory :\n\033[0m\n ")
directory = input()
subdirs = [x[0] for x in os.walk(directory)]
for x in subdirs:
    filedic = {**filedic, **hashfiles.gethashes(x + "/")}
print("\033[96m\n'files.json'\033[0m file created or overwritten in \033[92m'" + directory + "'\033[0m\n\n\033["
                                                                                            "94mBelow is what it "
                                                                                            "looks ""like:\n\033[0m")
print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in filedic.items()) + "}")
json = json.dumps(filedic)
f = open(directory + "/files.json","w")
f.write(json)
f.close()
