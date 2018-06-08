# machine-vision

batteries included machine vision classifier and analyzer.

## SMVC = Simple Machine Vision Classifier

Quick and dirty way to start

1. replace the images in SMVC/data/18060801-narrow_std/raw_images with your images representing _class 0_
2. replace the images in SMVC/data/18060802-wide_std/raw_images with your images representing _class 1_
3. delete the following folders: 
  - SMVC/data/18060801-narrow_std/training_images
  - SMVC/data/18060801-narrow_std/test_images
  - SMVC/data/18060801-wide_std/training_images
  - SMVC/data/18060801-wide_std/test_images
4. run SMVC/analysis/00_preprocess/main.py
  - this recreates the training and test sets
5. run SMVC/analysis/01_train/main.py
  - a classification map with red (class 0) and green (class 1) areas is created based on training set
  - training set is plotted with circles
  - the test set is plotted with squares
  
Example how this works is below. The _class 0_ training set consists of grayish images of sky, t-shirts, landscapes and  are depicted with red circles. Typically the standard deviation of the color intensity for these kind of images is low (as seen below). 

The _class 1_ training set consists of colorful pictures of balls, lights etc. and depicted with green squares. Typically the standard deviation for these kinds of pictures is large and varies a lot. 

The red and green areas depict the classification regions based on the training sets.

The red and green squares are then the test sets of similar images than in the training set (actually the images are divided in half and the upper left corner is the training set and lower right corner is the test set). There is no overlap between test and training sets.

The perfect clasificator would put all the red squares in the red area and green squares in the green area.

![](SMVC/results.png?raw=true)

