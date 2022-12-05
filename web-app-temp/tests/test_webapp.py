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

def test_book_path(flask_app):
    url = '/book'
    res = flask_app.get(url)
    assert res.request.path == url

def test_drums_status(flask_app):
    res=flask_app.get('/drums')
    assert res.status_code == 200

def test_drums_path(flask_app):
    url = '/drums'
    res = flask_app.get(url)
    assert res.request.path == url
    
def test_dumbbell_status(flask_app):
    res=flask_app.get('/dumbbell')
    assert res.status_code == 200
    
def test_dumbbell_path(flask_app):
    url = '/dumbbell'
    res = flask_app.get(url)
    assert res.request.path == url
    
def test_eyeglasses_status(flask_app):
    res=flask_app.get('/eyeglasses')
    assert res.status_code == 200

def test_eyeglasses_path(flask_app):
    url = '/eyeglasses'
    res = flask_app.get(url)
    assert res.request.path == url

def test_grapes_status(flask_app):
    res=flask_app.get('/grapes')
    assert res.status_code == 200

def test_grapes_path(flask_app):
    url = '/grapes'
    res = flask_app.get(url)
    assert res.request.path == url
    
def test_ladder_status(flask_app):
    res=flask_app.get('/ladder')
    assert res.status_code == 200

def test_ladder_path(flask_app):
    url = '/ladder'
    res = flask_app.get(url)
    assert res.request.path == url

def test_laptop_status(flask_app):
    res=flask_app.get('/laptop')
    assert res.status_code == 200

def test_laptop_path(flask_app):
    url = '/laptop'
    res = flask_app.get(url)
    assert res.request.path == url
    

