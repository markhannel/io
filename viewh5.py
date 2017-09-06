import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from lab_io import h5video as h5
import seaborn as sns
import cv2

def viewh5(filename, bgname, delta=1):
    sns.set(style='white', font_scale=1.4)
    bg = np.load(bgname)
    
    with h5.h5video(filename) as vid:
        # Get normalized image.
        norm = vid.get_image()/bg
        norm = norm[::delta, ::delta]

        # Start figure.
        fig = plt.figure()
        ax = plt.axes()
        #ax  = plt.axes(xlim=(0,1280), ylim=(0,1024/delta))
        ax.set_xlabel('X [pix]')
        ax.set_ylabel('Y [pix]')
        im = plt.imshow(norm, interpolation='none',
                        cmap=plt.get_cmap('gray'))


        def init():
            image = vid.get_image()/bg
            im.set_data(image[::delta, ::delta])

        def animate(i):
            norm = vid.next()/bg
            norm = norm[::delta, ::delta]
            im.set_array(norm)

        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=998, interval=1)

        plt.show()

def main():
    fn = 'example.h5'
    bgn = 'example_bg.npy'
    viewh5(fn, bgn)


    '''
    fn = 'data/x_00_00.h5'
    bgn = 'data/x_00_00.npy'
    viewh5(fn, bgn)
    '''
        
if __name__ == '__main__':
    main()
