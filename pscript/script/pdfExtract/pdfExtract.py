import os
import sys
import pdfplumber

sys.path.append(r'/home/liuwenwu/projects/pScriptFactory/')

from pscript.utils.paramPretreatment import *

class pdfEtractScript(lScript):
    def __init__(self,argv):
        super().__init__(argv)
        self.name = 'pdfExtract'
        self.description = '将pdf中的文本提取出来'
        self.version = '0.0.1'
        self.author = 'liuwenwu'
        self.author_email = 'liuawu625@163.com'
    
    def help(self):
        super().help()
        print("example:")
        print("pdfExtract /home/liuawu/Desktop/test.pdf")
        print('require one parameter:{pdfFile path}')
    
    def run(self):
        try:
            self.pdfFile = self.argv[0]
            with pdfplumber.open(self.pdfFile) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    print(text)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    pdfEtractScript(sys.argv[1:]).process()
    # with pdfplumber.open(r'/home/liuwenwu/Downloads/pdf/CQ11200509091700.pdf') as pdf:
    #     for page in pdf.pages:
    #         print(page.extract_text())