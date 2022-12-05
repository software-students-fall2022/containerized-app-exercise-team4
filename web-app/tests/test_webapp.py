import json


def test_index_status(flask_app):
    res = flask_app.get('/')
    assert res.status_code == 200
    
def test_index_path(flask_app):
    url = '/'
    res = flask_app.get(url)
    assert res.request.path == url

def test_leaderboard_status(flask_app):
    res=flask_app.get('/leaderboard')
    assert res.status_code == 200

def test_leaderboard_path(flask_app):
    url = '/leaderboard'
    res = flask_app.get(url)
    assert res.request.path == url

def test_active_status(flask_app):
    res=flask_app.get('/active')
    assert res.status_code == 200

def test_active_path(flask_app):
    url = '/active'
    res = flask_app.get(url)
    assert res.request.path == url
    
def test_statistics_status(flask_app):
    res=flask_app.get('/statistics')
    assert res.status_code == 200

def test_statistics_path(flask_app):
    url = '/statistics'
    res = flask_app.get(url)
    assert res.request.path == url
    
def test_baseball_status(flask_app):
    res=flask_app.get('/baseball')
    assert res.status_code == 200

def test_baseball_path(flask_app):
    url = '/baseball'
    res = flask_app.get(url)
    assert res.request.path == url
    
def test_anvil_status(flask_app):
    res=flask_app.get('/anvil')
    assert res.status_code == 200

def test_anvil_path(flask_app):
    url = '/anvil'
    res = flask_app.get(url)
    assert res.request.path == url

def test_book_status(flask_app):
    res=flask_app.get('/book')
    assert res.status_code == 200
