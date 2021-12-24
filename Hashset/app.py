import hashlib
import os

def compare(text, count):
    global cnt_hash

    for j in range(0, count):
        if text == hash_str[j]:
            cnt_hash = j
            return 1
        else:
            pass
    return 0

hash_str = {}
cnt = 0
cnt_hash = 0

file_name_read = input("파일명 입력 : ")
file_name_read += ".txt"
file_take = open(file_name_read, 'r')

while True:
    line = file_take.readline()
    if not line:
        break
    hash_str[cnt] = line
    cnt += 1

i = cnt
i -= 1

while i >= 0:
    hash_str[i] = hash_str[i][:-1]
    i -= 1

dirto = input("찾고 싶은 디렉토리 : ")
filelist = os.listdir(dirto)

for repeat in range(len(filelist)):
    with open(dirto+'/'+filelist[repeat], 'rb') as Filetake:
        file_reader = Filetake.read(4096)
    encoding = hashlib.md5()
    encoding.update(file_reader)
    encoding_text = encoding.hexdigest().upper()

    checking = compare(encoding_text, cnt)
    if checking:
        print("%s is the file match to hash [%s]"% (filelist[repeat], hash_str[cnt_hash]))
    else:
        pass
