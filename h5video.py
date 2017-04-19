import numpy as np
import h5py

class h5video(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.image = None
        self.index = None
        self.keys = self.f['images/'].keys()
        self.rewind()

    def __enter__(self):
        self.f = h5py.File(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        self.f.close()

    def view_image(self):
        try:
            self.image = self.f['images/' + self.keys[index]]
            return self.image
        except KeyError:
            print 'Indexed frame is not present.'

    def rewind(self):
        self.index = 0
        return self.view_image()

    def next(self):
        self.index += 1
        return self.image

    def goto(self, index):
        self.index = index
        

def example():
    import matplotlib.pyplot as plt

    # Grab h5 file.
    filename = 'x_00_00.h5'
    
    with h5video(filename) as vid:
        plt.imshow(vid.view_image)
        plt.show()

        vid.goto(100)
        
        plt.imshow(vid.view_image)
        plt.show()
    
if __name__ == '__main__':
    example()
