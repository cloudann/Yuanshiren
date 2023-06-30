import importlib as Import
import threading as thread
import random as ran
from cyaron import *
import copy
import subprocess as sub
import zipfile,os
_pre = 0
def choosen(lst):
   ran.shuffle(lst)
   return lst
def choosen_arr(lst,n):
   Lst = copy.deepcopy(lst)
   a = []
   for i in range(n):
      choosen(a)
      a.append(Lst.pop())
   return a
def make_matrix(n,m,order = True):
    if order:
        lst = list(range(1,n*m+1))
    else:
        lst = list(range(1,n*m*2))
        lst = choosen_arr(lst,n*m)
    choosen(lst)
    return get_arr(lst,n)
def get_arr(Arr,n):
    arr = copy.deepcopy(Arr)
    size = len(arr)
    lst = []
    l = []
    for i in range(size):
        choosen(arr)
        l.append(arr.pop())
        if i%n==n-1:
            lst.append(l)
            l = []
def per(id,tot):
    global _pre
    return int((id-_pre)/(tot-_pre)*100)
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
import copy
def get_arr(Arr,n):
    arr = copy.deepcopy(Arr)
    size = len(arr)
    lst = []
    l = []
    for i in range(size):
        next = choice(arr)
        del arr[arr.index(next)]
        l.append(next)
        if i%n==n-1:
            lst.append(l)
            l = []
    return lst
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
def rebuild(lst):
    arr = []
    for i in lst:
        if type(i)!=list:
            arr.append([i])
        else:
            for j in i:
                arr.append([j])
    return arr
            
def make_Big(left,right=0,neg = ""):
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
def low_set():
    return "".join([chr(ord("a")+i) for i in range(26)])
def upper_set():
    return "".join([chr(ord("A")+i) for i in range(26)])
class Test:
    import subprocess as sub
    example = None
    stderr = None
    stdout = None
    lst = []
    cmd = None
    pre = 0

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
    def Compile(self,remove = True):
        try:
            self.cmd(r'g++ Std/std.cpp -o Std/std')
            if remove:
                try:
                    a = self.sub.check_call(r'rm -rf test',shell = True,stdout=None)
                    print(s)
                except:
                    print("文件不存在")
                self.cmd(r'%s test'%(self.lst[0]))
        except:
            print("标程编译错误")
            return "标程编译错误"
        
    def remake_data(self,n = 16,pre = 0,close =False,prefix=""):
        global _pre
        _pre = pre
        self.Compile(False)
        
        for id in range(pre+1,n+1):
            next = str(id)
            if id<10:
                
                next = "0"+next
                print("test ",next)
                print(r'cp test/%s%s.in test/%d.back'%(prefix,next,id))
                try:
                    self.cmd(r'cp test/%s%s.in test/%d.back'%(prefix,next,id))
                except:
                    print("not 2")
            
            try:
                self.cmd(r'cp test/%s%d.in test/%d.back'%(prefix,id,id))
            except:
                print("not exist")
        for id in range(pre+1,n+1):
            next = id
            print("id: ",id)
            io = IO(file_prefix=r'test/', data_id=id)
            a = open(r'test/%d.back'%(id),"r")
            lst = a.readlines()
            a.close()
            self.cmd(r'rm test/%d.back')
            for i in range(len(lst)):
                lst[i] = [lst[i]]
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
        
    def make_data(self,n = 16,pre=0,func=print,close = False):
        name = func.__name__
        global _pre
        _pre = pre
        self.Compile()
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
            lst = rebuild(lst)
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
