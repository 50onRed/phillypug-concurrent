#!/bin/sh
import time
import socket

def non_gevent(host_names):
    start_time = time.time()
    host_ips = [socket.gethostbyname(host_name) for host_name in host_names]
    print host_ips
    return time.time() - start_time


if __name__ == '__main__':
    host_names = ['www.google.com', 'www.twitter.com', 'www.gevent.org', 'www.python.org']
    print 'Running code with blocking IO...'
    run_time = non_gevent(host_names)
    print 'Took %f.3 to run with blocking IO' % run_time
