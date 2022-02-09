#脚本的通用功能
#1、根据参数进行不同的操作
#2、输出帮助信息
#3、输出脚本的使用方法



class lScript:
    def __init__(self,argv):
        self.name = ''
        self.description = ''
        self.version = '0.0.1'
        self.author = 'liuwenwu'
        self.author_email = 'liuawu625@163.com'
        self.argv = argv
        self.argvLen = len(argv)
        self.argvDict = {}
        self.argvDict['-h'] = False
        self.argvDict['-help'] = False
        self.argvDict['-v'] = False
        self.argvDict['-info'] = False
        self.argvDict['--version'] = False
        self.argvDict['--help'] = False


    def process(self):
        if self.argvLen == 0:
            self.argvDict['-h'] = True
        for arg in self.argv:
            self.argvDict[arg] = True
        if self.argvDict['-h'] == True or self.argvDict['-help'] == True or self.argvDict['--help'] == True:
            self.help()
        elif self.argvDict['-v'] == True or self.argvDict['--version'] == True:
            self.info()
        elif self.argvDict['-info'] == True:
            self.info()
        else:
            self.run()

    def run(self):
        pass

    def help(self):
        print('usage: %s [options]' % self.name)
        print("\n")
        print(self.description)
        print("\n")
        print('options')
        print('-h,-help, --help: show help message')
        print('-v, --version: version information')
        print('-info: show script information')



    def info(self):
        print('name: %s' % self.name)
        print('description: %s' % self.description)
        print('version: %s' % self.version)
        print('author: %s' % self.author)
        print('author_email: %s' % self.author_email)