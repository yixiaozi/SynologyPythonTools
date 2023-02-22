#coding=utf-8
import os,sys,time

def list_files(startpath,exceptDirs):
    file = open(os.path.join(startpath,os.path.basename(startpath)+time.strftime('%Y-%m-%d %H%M%S',time.localtime(time.time()))+".txt"), "w")
    file.flush()
    for root, dirs, files in os.walk(startpath, topdown=True):
        #排除文件夹
        [dirs.remove(d) for d in list(dirs) if d in exceptDirs]
        level = root.replace(startpath, '').count(os.sep)
        indent =' '*4* (level-1)+'|'+'_' * 4
        file.writelines('{}{}/'.format(indent, os.path.basename(root)))
        file.writelines("\n")
        subindent = ' '*4* (level-1)+'|'+" "*6+"|"+"_"*4
        for f in files:
            file.writelines('{}{}'.format(subindent,  f))
            file.writelines("\n")
    file.close()

def write_unicode(text, charset='utf-8'):
    return text.encode(charset)

# list_files(write_unicode(u"A:\Docear"),[".svn"])

if __name__ == '__main__':
    rootPath=sys.argv[1]
    exceptDir=[]    #默认为空
    if len(sys.argv) > 2:
        exceptDir=sys.argv[2]
    list_files(write_unicode(rootPath), exceptDir)