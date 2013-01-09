import gevent
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()
import gzip
import time
import glob

def count_lines(path):
    lines = 0
    print 'Reading %s' % path
    with gzip.open(path, 'rb') as log_file:
        for line in log_file:
            lines += 1
    return lines

if __name__ == '__main__':
    paths = glob.glob('*.gz')#Change this to a path that has files with a .gz
                             #extension
    pool = Pool(8)
    start_time = time.time()
    jobs = [pool.spawn(count_lines, path) for path in paths]
    gevent.joinall(jobs)
    lines = 0
    for job in jobs:
        lines += job.value
    stop_time = time.time()
    print '\nFound %d lines in %.3fs' % (lines, stop_time - start_time)


