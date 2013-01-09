import gzip
import time
import glob
import threading
import Queue

class LineCounter(threading.Thread):

    def __init__(self, in_queue, out_queue, lock):
        super(LineCounter, self).__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.lock = lock

    def run(self):
        while True:
            path = self.in_queue.get()
            lines = 0
            lock.acquire()
            print 'Reading %s' % path
            lock.release()
            try:
                with gzip.open(path, 'rb') as log_file:
                    for line in log_file:
                        lines += 1
                self.out_queue.put(lines)
            finally:
                self.in_queue.task_done()


if __name__ == '__main__':
    paths = glob.glob('*.gz')
    lines = 0
    file_queue = Queue.Queue()
    line_count_queue = Queue.Queue()
    lock = threading.Lock()
    for i in xrange(8):
        thread = LineCounter(file_queue, line_count_queue, lock)
        thread.setDaemon(True)
        thread.start()
    start_time = time.time()
    for path in paths:
        file_queue.put(path)
    file_queue.join()
    while not line_count_queue.empty():
        lines += line_count_queue.get()
        line_count_queue.task_done()
    stop_time = time.time()
    print '\nFound %d lines in %.3fs' % (lines, stop_time - start_time)


