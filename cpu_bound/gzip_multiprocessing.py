import gzip
import time
import glob
import multiprocessing

def count_lines(path):
    lines = 0
    print 'Reading %s' % path
    with gzip.open(path, 'rb') as log_file:
        for line in log_file:
            lines += 1
    return lines

if __name__ == '__main__':
    paths = glob.glob('*.gz')
    pool = multiprocessing.Pool(8)
    start_time = time.time()
    results = pool.map(count_lines, paths)
    lines = sum(results)
    stop_time = time.time()
    print '\nFound %d lines in %.3fs' % (lines, stop_time - start_time)


