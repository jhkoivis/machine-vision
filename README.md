# machine-vision

batteries included machine vision classifier and analyzer.

## SMVC = Simple Machine Vision Classifier

Quick and dirty way to start

1. replace the images in SMVC/data/18060801-narrow_std/raw_images with your images representing _class 0_
2. replace the images in SMVC/data/18060802-wide_std/raw_images with your images representing _class 1_
3. delete the following folders: 
  SMVC/data/18060801-narrow_std/training_images
  SMVC/data/18060801-narrow_std/test_images
  SMVC/data/18060801-wide_std/training_images
  SMVC/data/18060801-wide_std/test_images
4. run SMVC/analysis/00_preprocess/main.py
  - this recreates the train and test sets
5. run SMVC/analysis/01_train/main.py
  - a classification map with red (class 0) and green (class 1) areas is created based on training set
  - training set is plotted with squares
  - the test set is plotted with circles
  



