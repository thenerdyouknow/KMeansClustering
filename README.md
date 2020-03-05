# K-Means Clustering in Python3

## Steps to run:
1. ```pip3 install -r requirements.txt```
2. ```python3 dataset_generator.py```
3. ```python3 final.py```

The program will cluster and then display the clusters as well. 

Note : The plotting of the clusters assumes that you're working with 2 dimensional data, if you'd like to work with more dimensions I would recomment using PCA to reduce the dimensions and then plotting it.

Note 2 : The distance is calculated using the Euclidean distance formula, that function can be replaced with one that calculated Manhattan distance as well. Will try to add that functionality in the future.

## Notes:
1. Datasets can be generated using dataset_generator.py
2. Sometimes the clustering won't be optimal, in which case try changing the random.seed at the beginning of the program and running it again.
3. Ideally, install the requirements in a virtual environment.
