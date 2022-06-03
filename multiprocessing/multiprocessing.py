from multiprocessing import cpu_count
from multiprocessing import Pool
import urllib.request as req
import cv2
import numpy as np
import os
import time


def read_url_image(args):
    url_response = req.urlopen(args[0])
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    return img



urls = ["https://images.accessgrantedonline.com/CAScanner1_256732.jpg",
"https://images.accessgrantedonline.com/CCC_0359.jpg",
"https://images.accessgrantedonline.com/CAScanner1_259233.jpg",
"https://images.accessgrantedonline.com/magma_249860.jpg",
"https://images.accessgrantedonline.com/magma_138419.jpg"]

fnames = ["CAScanner1_256732.jpg", "CCC_0359.jpg", "CAScanner1_259233.jpg", "magma_249860.jpg", "magma_138419.jpg"]


# So we’ll zip the urls and fns lists together to get a list of tuples.
inputs = zip(urls, fnames)


cpus = cpu_count()  # returns the number of processors that we can use.

save_path = 'test_images/bulk_save_test/'
iter = 0

if __name__ == '__main__':
    os.chdir(save_path)
    t0 = time.time()
    with Pool(processes= cpus-1 ) as pool:      

        for img in pool.imap_unordered(read_url_image, inputs):
            cv2.imwrite( str(iter) + ".jpg", img)
            iter += 1

    t1 = time.time()

    print("Time taken: ", str(t1-t0))
