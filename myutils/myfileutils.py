#https://k3no.medium.com/organizing-your-python-code-ca5445843368
#http://zetcode.com/lang/python/packages/
#os.path.splitext(file)[0]
import pandas as pd
import os, platform
from pathlib import Path

#get a list of files sorted by modified date
def getFilesByModTime(dir_path, reverse=False):
    modified=os.stat(dir_path).st_mtime
    return sorted(Path(dir_path).iterdir(), key=modified, reverse=reverse) 

def getFilesByCreateTime(dir_path, reverse=False):
    return sorted(Path(dirpath).iterdir(), key=getCreatdTime, reverse=reverse) 

def getCreatedTime(path_to_file):
   if platform.system() == 'Windows':
     return os.path.getctime(path_to_file)
   else:
      stat = os.stat(path_to_file)
      try:
        return stat.st_birthtime
      except AttributeError:
        #probably linux, no easy way to get creation date yet
        return stat.st_mtime

def retrieveCSVFileFromDir(src_dir='./csv', suffix='.csv', server_url='http://localhost:8002', target_dir='/target/', encoding='utf-8'):
  #
  for file in os.listdir(src_dir):
    if file.endswith(suffix):
        #print(os.path.join(suffix, file))
        url = server_url+os.path.splitext(file)[0]
        #print(url)
        df = pd.read_csv(url)
        df.to_csv(target_dir+file, encoding=encoding)

if __name__ == '__main__':
     pass
