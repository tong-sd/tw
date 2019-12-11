#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest

from functions import check_hemisphere

def test_it():
    assert check_hemisphere ('north') == 'Weather Condition: Cold during Winter Break'
    assert check_hemisphere ('south') == 'Weather Condition: Warm during Winter Break'

