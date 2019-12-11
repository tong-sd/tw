#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check_hemisphere(inpu):
    """
    
    Determine the weather condition of the city during Winter break
    by checking on which hemisphere it is.
    inpu: The expected input is the hemisphere (one of the instance attributes of city).
    
    """
    if inpu == 'north':
        outpu = 'Weather Condition: Cold during Winter Break'
    else:
        outpu = 'Weather Condition: Warm during Winter Break'
    return outpu

def check_dist(inpu):
    """
    
    Determine how far the city is from UCSD by checking the 
    distance of the city.
    inpu: The expected input is the position/distance (one of the instance attributes of city).
    
    
    """
    if inpu >= 7000:
        oupu = 'Distance Description: Far away from UCSD'
    if inpu < 7000 and inpu >= 3000:
        oupu = 'Distance Description: Not too far from UCSD'
    else:
        oupu = 'Distance Description: Close to UCSD'
    return oupu

def secret_mission(inpu):
    """

    Encoded the name of the city by using chr and ord with a key value.
    This is inspired by the similar function in A2.
    inpu: The expected input is the name (one of the instance attributes of city).
    
    """    
    key = 10
    encoded = ''
    for char in inpu:
        encoded = encoded + chr(ord(char) + 10)
    return encoded

class City():

    def __init__(self, name, position, hemisphere):
        """
        Parameters:
        -----------
        name: the name of the city
        
        position: the distance in miles of the city from UCSD
        
        hemisphere: the hemisphere on which the city is located on, 'north' or 'south'
    
        """
        self.name = name
        self.posi = position
        self.hemi = hemisphere

