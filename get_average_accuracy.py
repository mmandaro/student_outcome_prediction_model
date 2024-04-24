import numpy as np
import sklearn.model_selection
from sklearn.linear_model import LinearRegression


def get_average_accuracy(x, y, num_iterations=10):
    """Calculate the linear regression model's average accuracy after training it 'num_iterations' amount of times."""
    # Initialize a list to hold accuracy scores
    accuracy_scores = []

    # Run the model num_iterations amount of times
    for i in range(num_iterations):
        # Split the data into training and testing sets
        x_train, x_test, y_train, y_test, = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

        # Create/train linear regression model
        linear = LinearRegression()
        linear.fit(x_train, y_train)

        # Evaluate the model on the test set and store accuracy
        accuracy = linear.score(x_test, y_test)
        accuracy_scores.append(accuracy)

    # Calculate the average model accuracy
    average_accuracy = np.mean(accuracy_scores)
    return average_accuracy
