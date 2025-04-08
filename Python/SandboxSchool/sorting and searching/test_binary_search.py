from sandbox import binary_search



def test_binary_search():
    arr = [1, 3, 5, 7, 9, 11]

    assert binary_search(arr, 1) == 0  # First element
    assert binary_search(arr, 5) == 2  # Middle element
    assert binary_search(arr, 11) == 5  # Last element
    assert binary_search(arr, 4) == -1  # Not in list
    assert binary_search([], 5) == -1  # Empty list
    assert binary_search([10], 10) == 0  # Single element match
    assert binary_search([10], 5) == -1  # Single element no match