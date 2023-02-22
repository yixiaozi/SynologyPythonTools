import os,sys,shutil
class deletefile(object):
    def __init__(self,file):
        self.file=file
    def delete(self):
        print "Deleting %s" % self.file
        os.remove(self.file)
    def dryrun(self):
        print "Dry Run: %s [NOT DELETED]" % self.file
    def interactive(self):
        #answer=raw_input("Do you really want to delete: %s [Y/N]" % self.file)
        #if answer.upper() == 'Y':
         #   os.remove(self.file)
        #else:
         #   print "Skiping: %s" % self.file
        #os.remove(self.file)
        filepath = self.file
        if(not os.path.isdir(rootPath + "/" + "#recycle" + "/" + filepath[len(rootPath) + 1:len(filepath) - len(filepath.split("/")[-1])])):
            os.makedirs(rootPath + "/" + "#recycle" + "/" + filepath[len(rootPath) + 1:len(filepath) - len(filepath.split("/")[-1])],
                        0755)
        shutil.move(filepath,
                    rootPath + "/" + "#recycle" + "/" + filepath[len(rootPath) + 1:len(filepath) - len(filepath.split("/")[-1])])
        return

if __name__ == '__main__':
    from find_dupes import findDupes
    dup=findDupes(sys.argv[1])
    rootPath=sys.argv[2]
    for file in dup.iterkeys():
        delete=deletefile(file)
        #delete.dryrun()
        delete.interactive()
        #delete.delete()