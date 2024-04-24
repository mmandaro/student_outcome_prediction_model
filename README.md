Student Outcome Prediction Project:

Description:
The student outcome prediction project aims to assist educators in identifying at-risk students early, allowing for
improved intervention strategies to increase the overall passing rate. The project utilizes machine learning techniques,
specifically linear regression, to analyze student data and make a final grade prediction. By leveraging publicly
available data containing various student attributes such as prior grades, study time, failures, and more the project
trains a predictive model to forecast student's final grades. Educators can interact with the user interface to enter
data into the system and receive a prediction from the trained model.

Key Features:
-Utilizes the pandas library to read and preprocess student data from a CSV file.
-Selects relevant features for the machine learning model from the dataset.
-Utilizes numpy for its optimized array data structure to have more efficient calculations
-Splits the dataset into training and testing sets using scikitlearn's train_test_split function
-Trains a linear regression model on the data to predict students' final grades
-Calculates the accuracy of the trained model and provides insights into feature importance
-Provides an interactive user interface to input student data and receive predictions on their final grades
-Warns educators about students that are at-risk of failing based on the model's prediction

How to Use:
1. Ensure Python, numpy, pandas, and sklearn are all installed.
2. Clone the project to your local machine
3. Navigate to the project directory and run the main Python script
4. Follow the on-screen instructions for interacting with the user interface
5. Receive predictions on students' final grades