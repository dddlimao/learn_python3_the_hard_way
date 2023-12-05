import pytest
import sys
sys.path.append('..')
from NAME.name import AClass


def setup():
    print('SETUP!')

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")


