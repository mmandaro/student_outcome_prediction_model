# define the functions that create visualizations of the model and results

import matplotlib.pyplot as plt


# create a bar chart displaying feature importance, displaying how much influence each input variable has on predictions
def plot_feature_importance(feature_importance):
    plt.bar(range(len(feature_importance)), feature_importance, tick_label=["G1", "G2", "studytime", "failures",
                                                                            "absences", "famrel"])

    plt.xlabel("Features")
    plt.ylabel("Importance")
    plt.title("Feature Importance of Linear Regression Model")
    plt.show()


# create a scatterplot that showcases the actual grades vs the model's predicted grades
def plot_actual_vs_predicted(y_test, y_pred):
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Grades")
    plt.ylabel("Predicted Grades")
    plt.title("Actual vs. Predicted Grades")
    plt.show()


# create a histogram displaying the distribution of errors
def plot_distribution_of_errors(errors):
    plt.hist(errors, bins=20)
    plt.xlabel("Error")
    plt.ylabel("Frequency")
    plt.title("Distribution of Errors")
    plt.show()