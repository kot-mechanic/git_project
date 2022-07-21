# import os
#
# def find('_remote.repositories', 'D:\\work\\FORS\\OATI\\mos\\libs'):
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             return os.path.join(root, name)

import os, fnmatch
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

find('_remote.repositories', 'D:\work\FORS\OATI\mos\libs')