# acquire file for my world db mini project

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,recall_score,precision_score

import warnings
warnings.filterwarnings("ignore")


# Setting up the user credentials:

from env import host, user, password

def get_db(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# Acquiring the database:

def get_world_data(cache = False):
    
    world_all = '''
            SELECT c.*, cy.Name, cy.District, cy.Population, cl.Language, cl.Isofficial, cl.Percentage
            FROM country as c
            JOIN city AS cy ON c.code = cy.countrycode
            JOIN countrylanguage as cl ON c.code = cl.countrycode;
            '''
    
    
    filename = 'world_data.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql(world_all, get_db('world'))
        df.to_csv(filename, index = False)
        
    return df