import urllib
import json
import time
from contextlib import closing
import threading
import Queue
import os

class ImageDownloader(threading.Thread):
    def __init__(self, queue, lock):
        super(ImageDownloader, self).__init__()
        self.queue = queue
        self.lock = lock

    def run(self):
        while True:
            image_url = self.queue.get() #Blocks until an item is available
            try:
                filename = 'threading_images/' + image_url.rsplit('/', 1)[-1]
                self.lock.acquire()
                print 'Downloading %s...' % filename
                self.lock.release()
                with open(filename, 'wb') as file:
                    with closing(urllib.urlopen(image_url)) as response:
                        file.write(response.read())
            finally:
                self.queue.task_done()


def get_popular_instagram():
    client_id = '48e1929e1e1f48c2868d9851be981066'
    instagram_popular = 'https://api.instagram.com/v1/media/popular?'

    instagram_params = urllib.urlencode({'client_id': client_id})
    with closing(urllib.urlopen(instagram_popular + instagram_params)) as resp:
        instagram_data = json.loads(resp.read())
        return [entry['images']['low_resolution']['url'] for entry in instagram_data['data']]

if __name__ == '__main__':
    if not os.path.exists('threading_images'):
        os.mkdir('threading_images')
    image_urls = get_popular_instagram()
    queue = Queue.Queue()
    lock = threading.Lock()
    for i in xrange(8):
        thread = ImageDownloader(queue, lock)
        thread.setDaemon(True)
        thread.start()
    print 'Starting downloads...'
    start_time = time.time()
    for url in image_urls:
        queue.put(url)
    queue.join()
    stop_time = time.time()
    print 'Took %.3fs to download %d images' % (stop_time - start_time, len(image_urls))
