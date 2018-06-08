# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
import matplotlib.image as mpimg
from glob import glob
import numpy
import pylab

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def extract_features(im_name, label_id, feature_list, label_list):
    
    im = mpimg.imread(fn)
    
    # extract some features (e.g. std and median)
    # this could be changed or added to bubble radius etc.
    std = numpy.std(im[:,:,0])
    med = numpy.median(im[:,:,0])
    #mean = numpy.mean(im[:,:,0])
    
    # append features and labels to lists
    feature_list.append([std, med])
    label_list.append(label_id)


training_images = []
training_labels = []

test_images = []
test_labels = []

###########################################################
# air case: 0
###########################################################
for exp in ['../../data/18060801-narrow_std/',]:
    
    # training images
    for fn in glob(exp + '/training_images/*.jpg'):
        
        extract_features(fn, 0, training_images, training_labels)
        
    # test images
    for fn in glob(exp + '/test_images/*.jpg'):
        
        extract_features(fn, 0, test_images, test_labels)
        
##############################################################        
# ref case: 1        
################################################################
for exp in ['../../data/18060802-wide_std/',]:
    
    # training images
    for fn in glob(exp + '/training_images/*.jpg'):
        
        extract_features(fn, 1, training_images, training_labels)
        print(fn) 
        
    # test images
    for fn in glob(exp + '/test_images/*.jpg'):
        
        extract_features(fn, 1, test_images, test_labels)
    

training_images = numpy.array(training_images)
test_images = numpy.array(test_images)    

# initialize classifier
#classifier = svm.SVC()
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(3) #svm.SVC(C=1.0, gamma = 2)

print(training_images)
print(training_labels)

# train the classifiers
classifier.fit(training_images, training_labels)



print('#########################################################')
print('# check self consistency')
print('#########################################################')
# test classifier with same images
expected = training_labels
predicted = classifier.predict(training_images)
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

print('#########################################################')
print('# test with new images')
print('#########################################################')
# test classifier with new images
expected = test_labels
predicted = classifier.predict(test_images)
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


###############################################################
# the rest is just plotting
################################################################
    
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA']) #, '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00']) #, '#0000FF'])    

h = 0.1

x_min, x_max = training_images[:, 0].min() - 1, training_images[:, 0].max() + 1
y_min, y_max = training_images[:, 1].min() - 1, training_images[:, 1].max() + 1
xx, yy = numpy.meshgrid(numpy.arange(x_min, x_max, h),
                     numpy.arange(y_min, y_max, h))
Z = classifier.predict(numpy.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# plot training points
plt.scatter(training_images[:, 0], 
            training_images[:, 1], marker = 'o', c=training_labels, cmap=cmap_bold,
                edgecolor='k', s=20,
                label = 'training images')

# plot test points
plt.scatter(test_images[:, 0], 
            test_images[:, 1], marker = 's', c=test_labels, cmap=cmap_bold,
                edgecolor='k', s=20,
                label = 'test images')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

pylab.xlabel('std')
pylab.ylabel('median')

pylab.title('red: narrow std (grayish images)\n green: wide std (colorful images)')
pylab.legend()
plt.show()





