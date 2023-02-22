import os
import shutil
filepath=r"C:\yixiaozi\test\Newfolder\1.pdf"
path=r"C:\yixiaozi\test"
print(path+"\\"+"bin"+"\\"+filepath[len(path)+1:len(filepath)-len(filepath.split("\\")[-1])])
os.makedirs(path+"\\"+"bin"+"\\"+filepath[len(path)+1:len(filepath)-len(filepath.split("\\")[-1])],0755 )
shutil.move(filepath,path+"\\"+"bin"+"\\"+filepath[len(path)+1:len(filepath)-len(filepath.split("\\")[-1])])