#Author: Gentry Atkinson
#Organization: Texas University
#Data: 12 May, 2021
#Generate two Noise Not at Random label sets, 5% and 10%

#TODO:
#  -Make sure the feature extractor is the newest one
#  -Test the output
#  -Use the output of KNN to pick the noisy label

import numpy as np
from random import randint
import os
from sklearn.neighbors import NearestNeighbors
from utils.ts_feature_toolkit import get_features_for_set

def absChannels(X, num_channels):
    print("Length of attribute list in add_nnar: ", len(X))
    print("Length of signal in nnar: ", len(X[0]))
    print("Number of channels in nnar: ", num_channels)
    X_avg = np.zeros((len(X)//num_channels, len(X[0])))
    for i in range(0, len(X_avg)):
        X_avg[i, :] = np.linalg.norm(X[num_channels*i:num_channels*i+num_channels, :], axis=0)
    return X_avg

"""
Noise Not at Random-> the mislabeling rate is affected by class and features

Find instances of the majority class whose nearest neighbor in the extracted feature
space is not from the majority class. Relabel those instances as being from the minor
class. Other instances of the major class will have a uniform 3% mislabeling rate.
"""

# def add_nnar(attributes, clean_labels, filename, num_classes, num_channels=1, att_file=""):
#     low_noise_labels = np.copy(clean_labels)
#     high_noise_labels = np.copy(clean_labels)

#     if attributes == []:
#         print("reading attribute file")
#         attributes = np.genfromtxt(att_file, delimiter=',', dtype=int)

#     X = attributes

#     low_indexes = open(filename + '_nnar5_indexes.csv', 'w+')
#     high_indexes = open(filename + '_nnar10_indexes.csv', 'w+')

#     low_noise_file = open(filename + '_nnar5.csv', 'w+')
#     high_noise_file = open(filename + '_nnar10.csv', 'w+')

#     total_counter = 0
#     l_flipped_counter = 0
#     h_flipped_counter = 0

#     counts = [np.count_nonzero(clean_labels==i) for i in range(num_classes)]
#     MAJ_LABEL = int(np.argmax(counts))
#     MIN_LABEL = int(np.argmin(counts))
#     SET_LENGTH = len(clean_labels)

#     X = get_features_for_set(X)
#     X = np.reshape(attributes, (len(attributes)//num_channels, num_channels, len(attributes[0])))
#     print("feature extraction done")
#     nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(X[:, 0, :])
#     d, i = nbrs.kneighbors(X[:, 0, :])

#     while l_flipped_counter < 0.05*SET_LENGTH:
#         rand_instance_index = randint(0, SET_LENGTH-1)
#         total_counter += 1
#         if low_noise_labels[rand_instance_index] == MAJ_LABEL:
#             if low_noise_labels[i[rand_instance_index][1]]!=MAJ_LABEL or randint(0,99)<3:
#                 low_noise_labels[rand_instance_index] = MIN_LABEL
#                 l_flipped_counter += 1
#                 low_indexes.write('{}\n'.format(rand_instance_index))
#                 #print("Low noise flips: ", l_flipped_counter)

#     while h_flipped_counter < 0.1*SET_LENGTH:
#         rand_instance_index = randint(0, SET_LENGTH-1)
#         total_counter += 1
#         if high_noise_labels[rand_instance_index] == MAJ_LABEL:
#             if high_noise_labels[i[rand_instance_index][1]]!=MAJ_LABEL or randint(0,99)<3:
#                 high_noise_labels[rand_instance_index] = MIN_LABEL
#                 h_flipped_counter += 1
#                 high_indexes.write('{}\n'.format(rand_instance_index))
#                 #print("High noise flips: ", h_flipped_counter)


#     low_noise_file.write('\n'.join([str(int(i)) for i in low_noise_labels]))
#     high_noise_file.write('\n'.join([str(int(i)) for i in high_noise_labels]))
#     low_noise_file.write('\n')
#     high_noise_file.write('\n')


#     low_noise_file.close()
#     high_noise_file.close()

#     #sanity checks
#     print('---NNAR---')
#     print('Major label: ', MAJ_LABEL)
#     print('Minor label: ', MIN_LABEL)
#     print('Number of labels: ', SET_LENGTH)
#     print('Number of entries in neighbor table: ', len(i))
#     print('Size of neighbor vector: ', len(i[0]))
#     print('Total labels processed: ', total_counter)
#     print('Low noise labels flipped: ', l_flipped_counter)
#     print('High noise labels flipped: ', h_flipped_counter)
#     print('Length of low noise label set', len(low_noise_labels))
#     print('Length of high noise label set', len(high_noise_labels))
#     print('Lines written to low noise file: ')
#     os.system('cat {} | wc -l'.format(filename + '_nnar5.csv'))
#     print('Lines written to high noise file: ')
#     os.system('cat {} | wc -l'.format(filename + '_nnar10.csv'))

def add_nnar(
    attributes : np.ndarray, 
    clean_labels : np.ndarray, 
    filename : str, 
    num_classes : int,
    mislab_rate: int, 
    num_channels=1, 
    att_file="",
):
    """
    Write a noisy label file with a specific mislabeling rate (0-100)
    """
    if attributes==None:
        attributes = np.load(att_file)
    
    total_flipped = 0
    total_counter = 0

    counts = [np.count_nonzero(clean_labels==i) for i in range(num_classes)]
    MAJ_LABEL = int(np.argmax(counts))
    MIN_LABEL = int(np.argmin(counts))
    SET_LENGTH = len(clean_labels)

    attributes = get_features_for_set(attributes, len(attributes))
    noisy_labels = clean_labels.copy()

    nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(attributes)
    d, i = nbrs.kneighbors(attributes)

    while total_flipped < (mislab_rate/100)*SET_LENGTH:
        rand_instance_index = randint(0, SET_LENGTH-1)
        total_counter += 1
        if noisy_labels[rand_instance_index] == MAJ_LABEL:
            if noisy_labels[i[rand_instance_index][1]]!=MAJ_LABEL or randint(0,99)<(mislab_rate/10):
                noisy_labels[rand_instance_index] = MIN_LABEL
                total_flipped += 1

    np.save(f'{filename}_nnar_{mislab_rate}.npy', noisy_labels)

    #Sanity checks
    print('Len of clean labels: ', len(clean_labels))
    print('Len of noisy labels: ', len(noisy_labels))
    print('Mislabeling rate: ', mislab_rate)
    print('Number of noisy labels: ', total_flipped)
    print('Number of clean labels: ', np.count_nonzero(noisy_labels==clean_labels))

if __name__ == '__main__':
    clean_labels = np.concatenate((np.zeros((25000), dtype=int), np.ones((25000), dtype=int)), axis=0)
    add_nnar(clean_labels, 'test_labels', 2, 10)
    noisy_labels = np.load('test_labels_ncar_10.npy')
    
