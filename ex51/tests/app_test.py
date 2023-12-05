# from nose.tools import *
import pytest
from app import app

def assert_equal(actual,expected):
    assert actual == expected

def assert_in(actual,expected):
    assert actual in expected

app.config['TESTING'] = True
web = app.test_client() #Flask 自带的假的浏览器

def test_index():
    rv = web.get('/',follow_redirects=True)
    assert_equal(rv.status_code,404)

    rv = web.get('/hello',follow_redirects=True)
    assert_equal(rv.status_code,200)
    assert_in(b"Fill Out This Form",rv.data)

    data = {'name':'Zed','greet':'Hola'}
    rv = web.post('/hello',follow_redirects=True,data = data)
    assert_in(b"Zed",rv.data)
    assert_in(b"Hola",rv.data)
