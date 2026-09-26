from solution import fetch_profile, fetch_profiles_sequential, fetch_profiles_concurrent

def test_fetch_profile_with_single_number():

    expected = {"id": 1, "name": f"User {1}"}

    assert fetch_profile(1) == expected
    
def test_fetch_profile_with_sequential_order_preserved():

    input_sequence = [1, 2, 3, 4 ,5]
    expected_sequence = [{"id": 1, "name": f"User {1}"},
                {"id": 2, "name": f"User {2}"},
                {"id": 3, "name": f"User {3}"},
                {"id": 4, "name": f"User {4}"},
                {"id": 5, "name": f"User {5}"}]
    
    assert fetch_profiles_sequential(input_sequence) == expected_sequence

def test_fetch_profile_with_concurrent_order_preserved():

    input_sequence = [1, 2, 3, 4 ,5]
    expected_sequence_concurrent = [{"id": 1, "name": f"User {1}"},
                    {"id": 2, "name": f"User {2}"},
                    {"id": 3, "name": f"User {3}"},
                    {"id": 4, "name": f"User {4}"},
                    {"id": 5, "name": f"User {5}"}]
        
    assert fetch_profiles_concurrent(input_sequence, 3) == expected_sequence_concurrent

def test_sequential_and_concurrent():

    input_sequence = [1, 2, 3, 4 ,5]

    expected_result = [{"id": 1, "name": f"User {1}"},
                        {"id": 2, "name": f"User {2}"},
                        {"id": 3, "name": f"User {3}"},
                        {"id": 4, "name": f"User {4}"},
                        {"id": 5, "name": f"User {5}"}]

    assert fetch_profiles_sequential(input_sequence) == expected_result
    assert fetch_profiles_concurrent(input_sequence, 5) == expected_result 