from __future__ import unicode_literals
from os.path import abspath, join, dirname
import pandas as pd
import random


__title__ = 'ArabicNames'
__version__ = '0.1.0'
__author__ = 'Ahmed Madbouly'
__author_email__ = 'ahmedmadbouly@yahoo.com'
__license__ = 'MIT'

full_path = lambda filename: abspath(join(dirname(__file__), filename))

FILES = {
    'first': full_path('names.csv'),
    'last': full_path('lastnames.csv'),
}

firstName = pd.read_csv(FILES['first'])
lastName = pd.read_csv(FILES['last'])

def get_full_name():
    return firstName['Name'].sample().values[0] + ' ' + lastName['Name'].sample().values[0]
