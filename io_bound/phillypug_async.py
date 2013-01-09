import gevent
from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()
import urllib
import json
import time
import os
from contextlib import closing

def download_image(image_url):
    filename = 'async_images/' + image_url.rsplit('/', 1)[-1]
    print 'Downloading %s...' % filename
    with open(filename, 'wb') as file, closing(urllib.urlopen(image_url)) as response:
        file.write(response.read())


def get_popular_instagram():
    client_id = '48e1929e1e1f48c2868d9851be981066'

    instagram_popular = 'https://api.instagram.com/v1/media/popular?'

    instagram_params = urllib.urlencode({'client_id': client_id})
    with closing(urllib.urlopen(instagram_popular + instagram_params)) as resp:
        instagram_data = json.loads(resp.read())
        return [entry['images']['low_resolution']['url'] for entry in instagram_data['data']]

if __name__ == '__main__':
    if not os.path.exists('async_images'):
        os.mkdir('async_images')
    get_popular_job = gevent.spawn(get_popular_instagram)
    get_popular_job.join()
    image_urls = get_popular_job.value
    print 'Starting downloads...'
    start_time = time.time()
    pool = Pool(8)
    jobs = [pool.spawn(download_image, url) for url in image_urls]
    gevent.joinall(jobs)
    stop_time = time.time()
    print 'Took %.3fs to download %d images' % (stop_time - start_time, len(image_urls))
