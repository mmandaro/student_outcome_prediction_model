from display_user_interface import display_user_interface
from io import StringIO
import sys


def test_display_user_interface(capsys):
    """Tests the output of the 'test_display_user_interface' function."""
    # Store the expected output as a string
    expected_output = """\
************************************************
Welcome to the Student Outcome Prediction Model!
Please Select An Option:
Press 1 to test the model's accuracy.
Press 2 to see the average model accuracy.
Press 3 to input student data to predict final grade.
Press 4 to Exit
************************************************
"""

    # Capture the printed output
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function 'display_user_interface'
    display_user_interface()

    # Get the printed output
    printed_output = captured_output.getvalue()

    # Assert that the output matches the expected output
    assert printed_output == expected_output