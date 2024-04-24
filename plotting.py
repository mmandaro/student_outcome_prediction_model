import matplotlib.pyplot as plt


def plot_feature_importance(feature_importance):
    """Generates the feature importance plot."""
    plt.bar(range(len(feature_importance)), feature_importance, tick_label=["G1", "G2", "studytime", "failures",
                                                                            "absences", "famrel"])
    plt.xlabel("Features")
    plt.ylabel("Importance")
    plt.title("Feature Importance of Linear Regression Model")
    plt.show()


def plot_actual_vs_predicted(y_test, y_pred):
    """Generate scatterplot that showcases the actual grades vs the model's predicted grades."""
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Grades")
    plt.ylabel("Predicted Grades")
    plt.title("Actual vs. Predicted Grades")
    plt.show()


def plot_distribution_of_errors(errors):
    """Generate histogram showcasing the distribution of errors."""
    plt.hist(errors, bins=20)
    plt.xlabel("Error")
    plt.ylabel("Frequency")
    plt.title("Distribution of Errors")
    plt.show()