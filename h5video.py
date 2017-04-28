import numpy as np
import h5py

class h5video(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.image = None
        self.index = None
        self.dim = None
        self.nframes = None

    def __enter__(self):
        self.f = h5py.File(self.filename, self.mode)
        self.keys = self.f['images/'].keys()
        self.frames = self.f['images/'].values()
        self.nframes = len(self.frames)
        self.image = self.rewind()
        self.dim = self.f['images/' + self.keys[0]].shape
        return self

    def __exit__(self, *args):
        self.f.close()

    def get_image(self):
        try:
            self.image = self.frames[self.index]
            return self.image
        except KeyError:
            print 'Indexed frame is not present.'
            
    def get_time(self):
        return self.keys[self.index]

    def rewind(self):
        self.index = 0
        return self.get_image()

    def next(self):
        self.index += 1
        return self.get_image()

    def goto(self, index):
        self.index = index

def example():
    import matplotlib.pyplot as plt

    # Grab h5 file.
    filename = 'example.h5'
    bg = np.load('example_bg.npy')

    with h5video(filename) as vid:
        plt.imshow(vid.frames[-30]/bg)
        plt.gray()
        plt.show()

        plt.imshow(vid.get_image()/bg)
        plt.gray()
        plt.show()

        vid.goto(220)
        
        plt.imshow(vid.get_image()/bg)
        plt.gray()
        plt.show()
        
        print('Example timestamp: {}'.format(vid.get_time()))
        print('Dimension of image: {}'.format(vid.dim))
        print('Number of frames: {}'.format(vid.nframes))
    
if __name__ == '__main__':
    example()
