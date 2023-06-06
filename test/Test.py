
import importlib as Import
import threading as thread
from cyaron import *
class Test:
    import subprocess as sub
    import zipfile,os
    example = None
    stderr = None
    stdout = None
    cmd = None
    def Cmd(self,cmd):
        try:
            print(cmd)
            self.sub.check_call(cmd,shell="True")
        except:
            print("%s已存在"%(cmd))
    def __init__(self,lst=None,cmd = None):
        if cmd == None:
            cmd = self.Cmd
        #不通过文件则pip安装
        if lst ==None:
            lst = ["mkdir","touch"]
        self.cmd = cmd
        self.cmd(r'%s Std'%(lst[0]))
        self.cmd(r'%s test'%(lst[0]))
        self.cmd(r'%s Std\sample.py'%(lst[1]))
        self.cmd(r'%s Std\std.cpp'%(lst[1]))         
        try:
            self.example = Import.import_module("Std.sample")
        except:
            print("not")
    def mkzip(self,n = 16):
        a = self.sub.check_call(r'del test\new.zip',shell = True,stdout=None)
        
        zip_file = self.zipfile.ZipFile(r'test\new.zip','w')
        # 把zfile整个目录下所有内容，压缩为new.zip文件
        # zip_file.write('c.txt',compress_type=zipfile.ZIP_DEFLATED)
        for i in range(1,n):
            try:
                zip_file.write(r'test\test%d.in'%(i),compress_type=self.zipfile.ZIP_DEFLATED,arcname='test%d.in'%(i))
                zip_file.write(r'test\test%d.out'%(i),compress_type=self.zipfile.ZIP_DEFLATED,arcname='test%d.out'%(i))
            except:
                print("test%d不存在"%(i))
        zip_file.close()       
    
    def makedata(self,n = 16,func=None):
        try:
            #此处采用 reload 动态加载输入的函数模块
            if func == None:
                Import.reload(self.example)
                func = self.example.example
        except:
            print("example文件出错")
            return "example文件出错"
        #print(n,func,"end")
        try:
            self.cmd(r'mingw64\bin\g++.exe Std\std.cpp -o Std\std.exe')
        except:
            print("标程编译错误")
            return "标程编译错误"
        for id in range(1, n):
            print("id: ",id)
            io = IO(file_prefix=r'test\test', data_id=id)
            try:
                io = IO(file_prefix=r'test\test', data_id=id)
            except:
                #self.makedata(n,func)
                print("运行出错")
                return "运行出错"
            lst = func(id)
            print(lst)
            #m = randint(n - 1, MAXM) # DAG 的性质，边数大于等于节点数-1
            #graph = Graph.DAG(n, m) # n 点 m 边的 DAG
            if type(lst[0]) != list:
                lst = [lst]
            print("lst",lst)
            for i in lst:
                print(i)
                io.input_writeln(i)
            try:
                io.output_gen(r'Std\std.exe')
            except:
                print("标程运行错误")
                io.close()
                return  "标程运行错误"
            io.close()
        print("has end")
        zip = thread.Thread(target=self.mkzip,args=(n,))
        zip.start()
        zip.join()
        return "sucess"