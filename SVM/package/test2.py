# coding=utf-8

# write code...
import test
import codecs
import constfile_path as const
arra=[]
for i in xrange(10):
    arra.append(i)

fin=codecs.open(const.wolf_learn,'r',encoding="utf-8",errors="ignore")

for line in fin:
    print line
    array = line.split(",")

array=[i*2 for i in xrange(10)]
print arra
print array


test.fun()