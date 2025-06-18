# Import python libraries for data processing and visualisation
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import  warnings
warnings.filterwarnings("ignore")
#libraries imported to handle conll data
from collections import Counter
import itertools
from wordcloud import WordCloud

#NLP libraries
import nltk
import re
from nltk.corpus import stopwords
nltk.download('stopwords')

# Tensorflow import for model creation
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense, ReLU, Softmax, BatchNormalization, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

#sklearn for clustering and data visualisation
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

# Sklear imports for model evaluation
import sklearn.metrics as metrics

#Configurations
import yaml

# Load the YAML config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)



