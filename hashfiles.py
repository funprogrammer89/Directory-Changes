import os
import hashlib
def gethashes(path):
    filesANDfolders = os.listdir(path)
    filesHashList = list()
    files = [f for f in filesANDfolders if os.path.isfile(path + '/' + f)]  # Filtering only the files.
    fullFilePath = list()
    for x in files:
        fullFilePath.append(path +x)
        file = path  + x # Location of the file (can be set a different way)
        block_size = 65536 # The size of each read from the file
        file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file, 'rb') as f: # Open the file to read its bytes
            fb = f.read(block_size) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(block_size) # Read the next block from the file
        filesHashList.append(file_hash.hexdigest())
    file_dic = {}
    keys = fullFilePath
    values = filesHashList
    for i in range(len(values)):
        file_dic[keys[i]] = values[i]
    return file_dic
