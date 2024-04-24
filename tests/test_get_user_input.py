import pandas as pd
from io import StringIO
from get_user_input import get_user_input


def test_get_user_input(monkeypatch):
    """Test that 'get_user_input' correctly returns a data frame of user data."""
    # Initialize a sample dictionary of data
    sample_inputs = [
        '15',  # Grade 1
        '19',  # Grade 2
        '2',  # Study Time
        '1',  # Failures
        '4',  # Absences
        '3'  # Family Relationship
    ]

    # Mock the input function with monkeypatch to return sample inputs
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(sample_inputs)))

    # Call the function to test
    user_df = get_user_input()

    # Define the expected data frame based on the sample inputs
    expected_df = pd.DataFrame([{
        "G1": 15,
        "G2": 19,
        "studytime": 2,
        "failures": 1,
        "absences": 4,
        "famrel": 3
    }])

    # Assert that the actual DataFrame matches the expected DataFrame using the pandas method for more detailed testing
    pd.testing.assert_frame_equal(user_df, expected_df)




