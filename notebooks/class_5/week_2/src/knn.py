import numpy as np
import pandas as pd

class Knn_classification:

    def __init__(self):
        """
        Initialize the Knn class
        self.x_train: training data
        self.y_train: training labels
        """
        # Save the training data to properties of this class
        self.x_train = []
        self.y_train = []

    def fit(self, x, y):
        """
        Save the training data to properties of this class
        Parameters
        ----------
        x: training data
        y: training labels

        Returns
        -------
        None
        """
        self.x_train = x
        self.y_train = y

    def predict(self, x, k):
        """
        Predict the class labels for the provided data
        Parameters
        ----------
        x: data to classify
        k: number of neighbors to use

        Returns
        -------
        np.array(y_hat): array of predicted class labels
        """
        y_hat = []  # Variable to store the estimated class label
        # Calculate the distance from each vector in x to the training data
        
        # Calculate the distance between one observation and a list of observations
        def get_distance(x,X):
            diff = X - x
            return np.sum(diff**2, axis=1)
        
        def get_nearest(dist,k,labels):
            df_distance = pd.DataFrame({
                'distance':dist, 
                'y':labels
            })
            df_sorted = df_distance.sort_values('distance')
            return df_sorted['y'].iloc[0:k].values
        
        def get_most_frequent_class(labels):
            label_series = pd.Series(labels)
            df = label_series.value_counts()
            max_value = df.max()
            options = df[df==max_value].index.values
            return np.random.choice(options) # If there's one option, return it; else, pick one at random
        
        for v in x:
            distance = get_distance(v,self.x_train)
            nearest = get_nearest(distance,k,np.squeeze(self.y_train))
            class_estimate = get_most_frequent_class(nearest)
            y_hat.append(class_estimate)

        # Return the estimated targets
        return np.array(y_hat)
    
    
class Knn_regression:

    def __init__(self):
        """
        Initialize the Knn class
        self.x_train: training data
        self.y_train: training labels
        """
        # Save the training data to properties of this class
        self.x_train = []
        self.y_train = []

    def fit(self, x, y):
        """
        Save the training data to properties of this class
        Parameters
        ----------
        x: training data
        y: training labels

        Returns
        -------
        None
        """
        self.x_train = x
        self.y_train = y

    def predict(self, x, k):
        """
        Predict the class labels for the provided data
        Parameters
        ----------
        x: data to classify
        k: number of neighbors to use

        Returns
        -------
        np.array(y_hat): array of predicted class labels
        """
        y_hat = []  # Variable to store the estimated class label
        # Calculate the distance from each vector in x to the training data
        
        # Calculate the distance between one observation and a list of observations
        def get_distance(x,X):
            diff = X - x
            return np.sum(diff**2, axis=1)
        
        def get_nearest(dist,k,labels):
            df_distance = pd.DataFrame({
                'distance':dist, 
                'y':labels
            })
            df_sorted = df_distance.sort_values('distance')
            return df_sorted['y'].iloc[0:k].values
        
        def get_average_of_neighbors(values):
            return np.mean(values)
        
        for v in x:
            distance = get_distance(v,self.x_train)
            nearest = get_nearest(distance,k,np.squeeze(self.y_train))
            class_estimate = get_average_of_neighbors(nearest)
            y_hat.append(class_estimate)

        # Return the estimated targets
        return np.array(y_hat)