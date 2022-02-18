#提取pdf信息，并以csv格式，保存pdf名字，以及报告概况与企业基本信息
#!/usr/bin/env python3
# Path: pscript/script/pdfExtract/pdfExtract.py
# Compare this snippet from pscript/script/picIntoPdf/picIntoPdf.py:
import os
import sys
sys.path.append(r'/home/liuwenwu/projects/pScriptFactory/')

from pscript.script.pdfExtract.pdfExtract import pdfEtractScript

path="/home/liuwenwu/Downloads/pdf/"
savedStdout = sys.stdout
with open('/home/liuwenwu/Downloads/pdf/saved.csv', 'a+') as f:
    sys.stdout = f
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('pdf'):
                pdfEtractScript([os.path.join(root, file)]).process()
sys.stdout = savedStdout