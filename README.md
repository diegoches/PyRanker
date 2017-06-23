# PyRanker
Rank aggregation library in Python. PyRanker have implemented 12 different rank aggregation algorithms.

# The Rank Aggregation
The rank aggregation problem is to combine many different rank orderings on the same set of candidates, or alternatives, in order to obtain a “better” ordering. 

# Technical Pre-requisites
- Python 2.7

# Rank Aggregation Algorithms
PyRanker have the following algorithms implemented:
- FootRule
- Borda
- Copeland
- Median Rank
- MScores
- Reciprocal
- CombANZ
- CombMAX
- CombMIN
- CombMED
- CombMNZ
- CombSUM

# How to Install
In Linux/MacOS:
1. Install pip
2. Within a console, go to the PyRanker project folder.
3. Run: `pip install -r requirements.txt`


# Examples
- Loading Ranks:
´´´
from loaders.load_from_file import LoadFromFile
datasets = ['datasets/sample_1.txt', 'datasets/sample_2.txt', 'datasets/sample_3.txt']
rl = LoadFromFile.load_ranks(datasets)
´´´
