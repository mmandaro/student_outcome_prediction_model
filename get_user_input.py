# function that allows users to input student data to return a DataFrame for the prediction model

import pandas as pd


def get_user_input():
    # collect user input for each feature with input validation
    while True:
        try:
            g1 = int(input("Enter a value for Grade 1 (0-20): "))
            if 0 <= g1 <= 20:
                break
            else:
                print("Invalid input. Please enter an integer from 0 to 20.")
        except ValueError:
            print("Invalid input. Please enter an integer from 0 to 20.")

    while True:
        try:
            g2 = int(input("Enter a value for Grade 2 (0-20, if unavailable use grade 1 again): "))
            if 0 <= g2 <= 20:
                break
            else:
                print("Invalid input. Please enter an integer from 0 to 20.")
        except ValueError:
            print("Invalid input. Please enter an integer from 0 to 20.")

    while True:
        try:
            study_time = int(input("Next is student weekly study hours. Please enter a 1 for <2 hours, a 2 for"
                                   " 2 to 5 hours, a 3 for 5 to 10 hours, or a 4 for >10 hours: "))
            if 1 <= study_time <= 4:
                break
            else:
                print("Invalid input. Please enter an integer from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter an integer from 1 to 4.")

    while True:
        try:
            failures = int(input("Next is past class failures. Please enter the number of past class failures (if >=4, "
                                 " just enter 4): "))
            if 0 <= failures <= 4:
                break
            else:
                print("Invalid input. Please enter an integer from 0 to 4. If student has more than 4 failures, please"
                      " enter 4.")
        except ValueError:
            print("Invalid input. Please enter an integer from 0 to 4. If student has more than 4 failures, please"
                  " enter 4.")

    while True:
        try:
            absences = int(input("Please enter the student's number of absences (0-93): "))
            if 0 <= absences <= 93:
                break
            else:
                print("Invalid input. Please enter an integer from 0 to 93.")
        except ValueError:
            print("Invalid input. Please enter an integer from 0 to 93.")

    while True:
        try:
            family_rel = int(input("Lastly, enter the family relationship score (1-5) with 1 being very bad and 5 being"
                                   " excellent (if unavailable please enter 3): "))
            if 1 <= family_rel <= 5:
                break
            else:
                print("Invalid input. Please enter an integer from 1 to 5. If you are unsure, please enter 3.")
        except ValueError:
            print("Invalid input. Please enter an integer from 1 to 5. If you are unsure, please enter 3.")

    # create a dictionary of user inputs
    user_input_dict = {"G1": g1,
                       "G2": g2,
                       "studytime": study_time,
                       "failures": failures,
                       "absences": absences,
                       "famrel": family_rel
                       }

    # create a DataFrame from the user input dictionary
    user_df = pd.DataFrame([user_input_dict])

    return user_df
