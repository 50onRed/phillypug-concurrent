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
    paths = glob.glob('*.gz')
    lines = 0
    start_time = time.time()
    for path in paths:
        lines += count_lines(path)
    stop_time = time.time()
    print '\nFound %d lines in %.3fs' % (lines, stop_time - start_time)


