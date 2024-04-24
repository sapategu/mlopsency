import os, urllib.request, zipfile
from pathlib import Path
from typing import Dict

_DATASET_ENDPOINT = Path(__file__).resolve().parent.parent / 'datasets/'

class DATASETS:
   MNIST: Dict = {
      'train_images': 'http://yann.lecun.org/exdb/mnist/train-images-idx3-ubyte.gz',
      'train_labels': 'http://yann.lecun.org/exdb/mnist/train-labels-idx1-ubyte.gz',
      'test_images': 'http://yann.lecun.org/exdb/mnist/t10k-images-idx3-ubyte.gz',
      'test_labels': 'http://yann.lecun.org/exdb/mnist/t10k-labels-idx1-ubyte.gz'
   }
   
   NORB: Dict = {
      'train_01': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-01-dat.mat.gz',
      'train_02': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-02-dat.mat.gz',
      'train_03': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-03-dat.mat.gz',
      'train_04': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-04-dat.mat.gz',
      'train_05': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-05-dat.mat.gz',
      'train_06': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-06-dat.mat.gz',
      'train_07': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-07-dat.mat.gz',
      'train_08': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-08-dat.mat.gz',
      'train_09': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-09-dat.mat.gz',
      'train_10': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x46789x9x18x6x2x108x108-training-09-dat.mat.gz',
      'test_01': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x01235x9x18x6x2x108x108-testing-01-dat.mat.gz',
      'test_02': 'https://cs.nyu.edu/~ylclab/data/norb-v1.0/norb-5x01235x9x18x6x2x108x108-testing-02-dat.mat.gz',
   }


def rps_download():
   print("Download RPS Dataset, Hold a sec.....")
   data_url = 'https://github.com/dicodingacademy/assets/releases/download/release-rps/rps.zip'
   urllib.request.urlretrieve(data_url, _DATASET_ENDPOINT / 'rps.zip')
   local_file = 'rps.zip'
   zip_ref = zipfile.ZipFile(_DATASET_ENDPOINT / local_file, 'r')
   zip_ref.extractall(_DATASET_ENDPOINT)
   zip_ref.close()
   os.remove(_DATASET_ENDPOINT / local_file)
   print("Download RPS Dataset completed!!")
   
def mnist_download():
   pass

def norb_download():
   pass