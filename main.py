# Morgan Mandaro
# C964 Computer Science Capstone
# Linear Regression Model to Predict Student Outcomes

import pandas as pd
import numpy as np
import sklearn
import plotting
import warnings
from sklearn.linear_model import LinearRegression
from display_user_interface import display_user_interface
from get_average_accuracy import get_average_accuracy
from get_user_input import get_user_input

# use pandas library to read the csv file into a DataFrame and change separator to ';' to match the data
student_data = pd.read_csv('data/student-mat.csv', sep=";")

# assign our features we want for the model
selected_features = ["G1", "G2", "G3", "studytime", "failures", "absences", "famrel"]

# create a new DataFrame containing only the desired data
student_data = student_data[selected_features]

# set prediction label to 'G3', the students final grade
predict = "G3"

# define feature matrix 'x' and prepare it for the machine learning model by removing 'G3' the target variable column
x = np.array(student_data.drop(columns=[predict]))

# define and prepare target variable for the machine learning model using only 'G3' column
y = np.array(student_data[predict])

# use sklearn's train_test_split function to split the data into a training set and a testing set
# source: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
x_train, x_test, y_train, y_test, = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# instantiate the linear regression model
# source: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
linear = LinearRegression()

# fit the model to the training data
linear.fit(x_train, y_train)

# use the model to make predictions on the test set
y_pred = linear.predict(x_test)

# use the model to get feature importance
feature_importance = linear.coef_

# calculate the errors
errors = y_test - y_pred

# use the score method to evaluate the accuracy of the trained linear regression model
model_accuracy = linear.score(x_test, y_test)

# turn the model accuracy into a percentage with 1 decimal place for better readability
model_accuracy_percentage = round(model_accuracy * 100, 1)

# use the display_user_interface function to display the user interface
display_user_interface()

# get user input to branch program appropriately
user_choice = int(input("Enter Choice Here: "))

print("You entered: ", user_choice)

# get user input until they enter 4 to exit
while user_choice != 4:

    if (user_choice < 0) or (
            user_choice > 4):  # If the user input is not between 1 and 4 inclusive, this branch is taken
        print("Invalid Entry, Please Try Again. Must be 1-4.")  # Prints out error message for invalid input
        user_choice = int(input("Input: "))  # Takes in a new user input
        while (user_choice < 1) or (user_choice > 4):  # Repeats the above so long as an invalid input is received
            print("Invalid Entry, Please Try Again")
            user_choice = int(input("Input: "))

    if user_choice == 0:
        display_user_interface()
        user_choice = int(input("Enter Choice Here: "))

    if user_choice == 1:  # if the user input a 1, display the current model accuracy
        print("Model Accuracy: ", model_accuracy_percentage, "%")
        print()
        user_choice = int(input("Enter Next Choice Here (enter 0 to see the options again): "))
        print("You entered: ", user_choice)

    elif user_choice == 2:  # if the user input a 2, display the average model accuracy
        avg_model_accuracy = get_average_accuracy(x, y)  # use function to calculate the model's avg accuracy
        print(f"Average Model Accuracy: {avg_model_accuracy * 100:.1f}%")  # output formatted avg model accuracy
        print()
        user_choice = int(input("Enter Next Choice Here (enter 0 to see the options again): "))
        print("You entered: ", user_choice)

    elif user_choice == 3:  # if the user input a 3, collect student data to make a prediction using the model
        # call get_user_input to return a DataFrame containing the user's input student data
        user_df = get_user_input()

        # suppress the UserWarning generated due to the model not having feature names. The model works as intended.
        warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

        # use the model to predict G3 for the user's input
        user_prediction = linear.predict(user_df)

        # change the grade to a percentage for enhanced readability
        grade_percentage = (user_prediction[0] / 20) * 100

        # print the predicted grade for G3 for the user's input
        print() # line of whitespace for improved readability
        print(f"Predicted final grade: {grade_percentage: .1f}%", )

        # if predicted grade is a failing grade, output a warning to the user
        if grade_percentage < 70:
            print("Warning: student is at risk of failing.")
        else:
            print("Student not at risk of failing.")
        print()

        user_choice = int(input("Enter Next Choice Here (enter 0 to see the options again): "))
        print("You entered: ", user_choice)

print("Ending Program, please wait for the data visualizations to load.")  # output end program message

# create visualizations using the functions from plotting.py
plotting.plot_feature_importance(feature_importance)
plotting.plot_actual_vs_predicted(y_test, y_pred)
plotting.plot_distribution_of_errors(errors)

