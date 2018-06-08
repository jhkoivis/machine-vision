
import pylab
#import rawpy
from glob import glob
import os

expList = ['../../data/18060801-narrow_std/',
           '../../data/18060802-wide_std/']

xmin    = 0
xmax    = 1000
ymin    = 0
ymax    = 1000

width   = 100
height  = 100





for exp in expList: #[1:]: #[:1]:
    for fn in glob(exp + '/raw_images/*.jpg'):
        
        print(fn)
        
        try:
            os.makedirs(os.path.dirname(fn) + '/../training_images')#, exists_ok = True)
        except:
            pass
        try:
             os.makedirs(os.path.dirname(fn) + '/../test_images')#, exists_ok = True)
        except:
            pass    
             
        #raw = rawpy.imread(fn)
        #bayer = raw.raw_image 
        bayer = pylab.imread(fn)
        
        
        pylab.imshow(bayer)
        
        print(bayer.shape)
        
        

            
        for i in range(xmin,xmax,width):
            for j in range(ymin, ymax, height):
        
        
                try:
                    if i > j:
                        train_01    = bayer[j:j+height, i:i+width]  
                        if train_01.shape[0] > 0 and train_01.shape[1] > 0:
                            train_01_fn = fn.replace('raw_images', 'training_images').replace('.jpg', '-train_01_%d_%d.jpg' % (i,j))
                            pylab.imsave(train_01_fn, train_01)                
                except:
                    pass
                
                try:
                    if j > i:
                        test_02     = bayer[j:j+height, i:i+width]
                        if test_02.shape[0] > 0 and test_02.shape[1] > 0:
                            test_02_fn = fn.replace('raw_images', 'test_images').replace('.jpg', '-test_02_%d_%d.jpg' % (i,j))
                            pylab.imsave(test_02_fn, test_02)
                except:
                    pass

        

        #pylab.show()