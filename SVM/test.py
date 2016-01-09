import numpy


def fun():
    print "d"

print "aaa"



if __name__ == '__main__':
    array = [0,1,2,3,4]
    mean = numpy.mean(array)
    var = numpy.std(array)

    print str(mean) + " " + str(var)
    array2 = []
    for i in xrange(5):
        array2.append((array[i] - mean)/var)
    print array2
    print numpy.std(array2)
print "aaa"
