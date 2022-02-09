#将当前文件夹内的所有图片转换为pdf并合并为一个pdf

import os
import sys
sys.path.append(r'/home/liuwenwu/projects/pScriptFactory/')
  
from pscript.utils.paramPretreatment import *

class picIntoPdfScript(lScript):
    def __init__(self,argv):
        super().__init__(argv)
        self.name = 'picIntoPdf'
        self.description = '将当前文件夹内的所有图片(jpg png)转换为pdf并合并为一个pdf'
        self.version = '0.0.1'
        self.author = 'liuwenwu'
        self.author_email = 'liuawu625@163.com'

    def help(self):
        super().help()
        print("example:")
        print("picIntoPdf /home/liuawu/Desktop/imageDir")
        print('require one parameter:{directory path}')
    
    def run(self):
        self.path = self.argv[0]
        print(self.path)
        self.convert_to_pdf()
        self.merge_pdf()
        self.remove_pdf()



    def convert_to_pdf(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.jpg') or file.endswith('.png'):
                    os.system('convert %s %s.pdf' % (os.path.join(root, file), os.path.join(root, file[:-4])))
            for file in dirs:
                if file.endswith('.jpg') or file.endswith('.png'):
                    os.system('convert %s %s.pdf' % (os.path.join(root, file), os.path.join(root, file[:-4])))

    def merge_pdf(self):
        tmpFileList= ""
        fileList = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                print(file)
                if file.endswith('.pdf'):
                    fileList.append(os.path.join(root, file))
            for file in dirs:
                if file.endswith('.pdf'):
                    fileList.append(os.path.join(root, file))
        #对fileList按照文件名进行字母排序
        fileList.sort(key=lambda x: x[-10:])
        for file in fileList:
            tmpFileList += os.path.join(root, file) + " "
        os.system('pdfunite %s %s' % (tmpFileList, os.path.join(self.path, 'merge.pdf')))

    def remove_pdf(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.pdf') and file != 'merge.pdf':
                    os.remove(os.path.join(root, file))
            for file in dirs:
                if file.endswith('.pdf') and file != 'merge.pdf':
                    os.remove(os.path.join(root, file))


if __name__ == '__main__':
    picIntoPdfScript(sys.argv[1:]).process()