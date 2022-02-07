#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:46:38 2022

@author: harshitpandey
"""

from pydantic import BaseModel

class BankNote(BaseModel):
    variance: float
    skewness: float
    cutosis: float
    entropy: float