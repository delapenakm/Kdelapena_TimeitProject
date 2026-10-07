
import pytest

from searchFunctions import (
    linear_search,
    binary_search,
    interpolation_search
)

#---------------------------------------------------------------------------
# TESTING linear_search()
#---------------------------------------------------------------------------
def test_linear_search_found():
    """Ensure that designated value's position is returned when found"""
    list = [1, 2, 3, 4, 5]

    assert linear_search(list, 2) == 1

def test_linear_search_not_found():
    """Ensure that -1 is returned when designated value not in list"""
    list = [1, 2, 3, 4, 5]

    assert linear_search(list, 6) == -1

def test_linear_search_beginning():
    """Ensure value at beginning edge case is returned as index 0"""
    list = [1, 2, 3, 4, 5]

    assert linear_search(list, 1) == 0

def test_linear_search_end():
    """Ensure value at end edge case is returned as index 4"""
    list = [1, 2, 3, 4, 5]
    
    assert linear_search(list, 5) == 4

def test_linear_search_middle():
    """Ensure middle value is returned at index 2"""
    list = [1, 2, 3, 4, 5]
        
    assert linear_search(list, 3) == 2

#---------------------------------------------------------------------------
# TESTING binary_search()
#---------------------------------------------------------------------------
def test_binary_search_found():
    """Ensure that designated value's position is returned when found"""
    list = [1, 2, 3, 4, 5]

    assert binary_search(list, 2) == 1

def test_binary_search_not_found():
    """Ensure that -1 is returned when designated value not in list"""
    list = [1, 2, 3, 4, 5]

    assert binary_search(list, 6) == -1

def test_binary_search_beginning():
    """Ensure value at beginning edge case is returned as index 0"""
    list = [1, 2, 3, 4, 5]

    assert binary_search(list, 1) == 0

def test_binary_search_end():
    """Ensure value at end edge case is returned as index 4"""
    list = [1, 2, 3, 4, 5]
    
    assert binary_search(list, 5) == 4

def test_binary_search_middle():
    """Ensure middle value is returned at index 2"""
    list = [1, 2, 3, 4, 5]
        
    assert binary_search(list, 3) == 2

#---------------------------------------------------------------------------
# TESTING interpolation_search()
#---------------------------------------------------------------------------
def test_interpolation_search_found():
    """Ensure that designated value's position is returned when found"""
    list = [1, 2, 3, 4, 5]

    assert interpolation_search(list, 2) == 1

def test_interpolation_search_not_found():
    """Ensure that -1 is returned when designated value not in list"""
    list = [1, 2, 3, 4, 5]

    assert interpolation_search(list, 6) == -1

def test_interpolation_search_beginning():
    """Ensure value at beginning edge case is returned as index 0"""
    list = [1, 2, 3, 4, 5]

    assert interpolation_search(list, 1) == 0

def test_interpolation_search_end():
    """Ensure value at end edge case is returned as index 4"""
    list = [1, 2, 3, 4, 5]
    
    assert interpolation_search(list, 5) == 4

def test_interpolation_search_middle():
    """Ensure middle value is returned at index 2"""
    list = [1, 2, 3, 4, 5]
        
    assert interpolation_search(list, 3) == 2