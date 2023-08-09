import pytest
import assessment as assess
import numpy as np

def test_remove_greater_than():
    threshold = 20
    case1 = { 'input': np.array([1,2,20,21,20000]),
              'output': np.array([1,2,20])}
    output = assess.remove_greater_than(case1['input'], threshold) 
    assert len(output) == len(case1['output']), "remove_greater_than(): Size not the same"                  
    assert np.equal(output,case1['output']).all(), "remove_greater_than(): Values not the same"

def test_remove_less_than():
    threshold = 20
    case1 = { 'input': np.array([1,2,20,21,20000]),
              'output': np.array([20,21,20000])}
    output = assess.remove_less_than(case1['input'], threshold) 
    assert len(output) == len(case1['output']), "remove_less_than(): Size not the same"                  
    assert np.equal(output,case1['output']).all(), "remove_less_than(): Values not the same"

def test_remove_if_equal():
    value_list = [2,20,21]
    case1 = { 'input': np.array([1,2,20,21,20000]),
              'output': np.array([1,20000])}
    output = assess.remove_if_equal(case1['input'], value_list) 
    assert len(output) == len(case1['output']), "remove_if_equal(): Size not the same"                  
    assert np.equal(output,case1['output']).all(), "remove_if_equal(): Values not the same"

def test_remove_duplicates():
    case1 = { 'input': np.array([1,1,2,2,2,2,20,21,21,21,21,21,20000]),
              'output': np.array([1,2,20,21,20000])}
    output = assess.remove_duplicates(case1['input']) 
    assert len(output) == len(case1['output']), "remove_duplicates(): Size not the same"                  
    assert np.equal(output,case1['output']).all(), "remove_duplicates(): Values not the same"