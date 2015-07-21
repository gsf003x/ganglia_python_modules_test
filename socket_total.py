#!/usr/bin/python

from subprocess import Popen, PIPE

def socket_handler(name):
    # "lsof -i | wc -l" is the shell commend I use to get metric value
    p = Popen("lsof -i | wc -l", stdout = PIPE, shell = True)
    output = p.communicate()[0]
    ret = float(output)
    if ret != 0:
	ret -= 1
    return ret
    

def metric_init(params):
    global descriptors

    d1 = {'name': 'socket_total',
        'call_back': socket_handler,
        'time_max': 30,
        'value_type': 'float',
        'units': '',
        'slope': 'both',
        'format': '%f',
        'description': 'Number of sockets connetions',
        'groups': 'network'}

    descriptors = [d1]

    return descriptors

def metric_cleanup():
    '''Clean up the metric module.'''
    pass

#This code is for debugging and unit testing
if __name__ == '__main__':
    metric_init({})
    for d in descriptors:
        v = d['call_back'](d['name'])
        print 'value for %s is %f' % (d['name'],  v)
