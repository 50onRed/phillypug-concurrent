#!/bin/sh
import time
import gevent
from gevent import monkey
monkey.patch_all()
import socket

def gevent_io(host_names):
    start_time = time.time()
    jobs = [gevent.spawn(socket.gethostbyname, host_name) for host_name in host_names]
    gevent.joinall(jobs, raise_error=True)
    host_ips = [job.value for job in jobs]
    print host_ips
    return time.time() - start_time

if __name__ == '__main__':
    host_names = ['www.google.com', 'www.twitter.com', 'www.gevent.org', 'www.python.org']
    print 'Running code with non-blocking IO...'
    gevent_run_time = gevent_io(host_names)
    print 'Took %f.3 to run with non-blocking IO' % gevent_run_time
