# define function to return the average model accuracy

import numpy as np
import sklearn.model_selection
from sklearn.linear_model import LinearRegression


def get_average_accuracy(x, y, num_iterations=10):
    accuracy_scores = []  # initialize a list to hold accuracy scores

    # run the model num_iterations amount of times
    for i in range(num_iterations):
        # split the data into training and testing sets
        x_train, x_test, y_train, y_test, = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

        # create/train linear regression model
        linear = LinearRegression()
        linear.fit(x_train, y_train)

        # evaluate the model on the test set and store accuracy
        accuracy = linear.score(x_test, y_test)
        accuracy_scores.append(accuracy)

    # calculate the average model accuracy
    average_accuracy = np.mean(accuracy_scores)
    return average_accuracy
