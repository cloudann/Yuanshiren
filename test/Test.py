import importlib as Import
import threading as thread
from cyaron import *

import subprocess as sub
import zipfile,os
def per(id,tot):
    return int(id/tot*100)
def check(file):
    x = file.readlines()
    for i in x:
        p = i.split(" ")
        for j in p:
            try:
                if float(j)<0:
                    return True
            except:
                1
    return False
def mkzip(n = 16,pre = 0,name = "new"):
    zip_file = zipfile.ZipFile(r'test/%s.zip'%(name),'w')
    # 把zfile整个目录下所有内容，压缩为new.zip文件
    # zip_file.write('c.txt',compress_type=zipfile.ZIP_DEFLATED)
    for i in range(pre+1,n):
        try:
            a = open(r'test/%d.out'%(i),"r")
            #print("check is ",check(a))
            if check(a):
                print(r'test/%d.out has a negative value'%(i))
            a.close()
       
            zip_file.write(r'test/%d.in'%(i),compress_type=zipfile.ZIP_DEFLATED,arcname='%d.in'%(i))
            zip_file.write(r'test/%d.out'%(i),compress_type=zipfile.ZIP_DEFLATED,arcname='%d.out'%(i))
        except:
            print("test%d不存在"%(i))
        sub.check_call(r'rm test/%d.in'%(i),shell = True,stdout=None)
        sub.check_call(r'rm test/%d.out'%(i),shell = True,stdout=None)
    zip_file.close()     
    print("finish")

def make_Big(self,left,right=0,neg = ""):
    if right ==0:
        right = left
    if neg:
        neg = '-'
    bit_set = "".join([str(i) for i in range(10)])
    begin = "%s%s"%(bit_set[1:],neg)
    begin = String.random((1),charset = begin)
    if begin !="-":
        left-=1
        left= max(left,0)
        right-=1
        right = max(right,0)
    print(left,right)
    return "%s%s"%(begin,String.random((left,right),charset = bit_set))
class Test:
    import subprocess as sub
    example = None
    stderr = None
    stdout = None
    lst = []
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
        self.lst = lst
        self.cmd = cmd
        self.cmd(r'%s Std'%(lst[0]))
        self.cmd(r'%s Std/sample.py'%(lst[1]))
        self.cmd(r'%s Std/std.cpp'%(lst[1]))         
        try:
            self.example = Import.import_module("Std.sample")
        except:
            print("not")
    def make_data(self,n = 16,pre=0,func=print,close = False):
        name = func.__name__
        try:
            self.cmd(r'g++ Std/std.cpp -o Std/std')
            try:
                a = self.sub.check_call(r'rm -rf test',shell = True,stdout=None)
            except:
                print("文件不存在")
       
            self.cmd(r'%s test'%(self.lst[0]))
        except:
            print("标程编译错误")
            return "标程编译错误"
        for id in range(pre+1, n+1):
            print("id: ",id)
            io = IO(file_prefix=r'test/', data_id=id)
            try:
                io = IO(file_prefix=r'test/', data_id=id)
            except:
                #self.makedata(n,func)
                print("运行出错")
                return "运行出错"
            lst = func(id,n)
            #m = randint(n - 1, MAXM) # DAG 的性质，边数大于等于节点数-1
            #graph = Graph.DAG(n, m) # n 点 m 边的 DAG
            if type(lst[0]) != list:
                lst = [lst]
            for i in lst:
                io.input_writeln(i)
            try:
                io.output_gen(r'Std/std')
            except:
                print("标程运行错误")
                io.close()
                return  "标程运行错误"
            io.close()
        print("has end")
        if close:
            return "success"
        zip = thread.Thread(target=mkzip,args=(n+1,pre))
        zip.start()
        zip.join()
        return "success"
