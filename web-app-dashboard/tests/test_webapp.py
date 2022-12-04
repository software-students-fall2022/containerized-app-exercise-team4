import json


def test_index_status(app, client):
    res = client.get('/')
    assert res.status_code == 200
    
def test_index_path(app, client):
    url = '/'
    res = client.get(url)
    assert res.request.path == '/'

def test_leaderboard_status(app, client):
    res=client.get('/leaderboard')
    assert res.status_code == 200

def test_leaderboard_path(app, client):
    url = '/leaderboard'
    res = client.get(url)
    assert res.request.path == '/leaderboard'

def test_active_status(app, client):
    res=client.get('/active')
    assert res.status_code == 200

def test_active_path(app, client):
    url = '/active'
    res = client.get(url)
    assert res.request.path == '/active'
    
def test_statistics_status(app, client):
    res=client.get('/statistics')
    assert res.status_code == 200

def test_statistics_path(app, client):
    url = '/statistics'
    res = client.get(url)
    assert res.request.path == '/statistics'
    
def test_baseball_status(app, client):
    res=client.get('/baseball')
    assert res.status_code == 200

def test_baseball_path(app, client):
    url = '/baseball'
    res = client.get(url)
    assert res.request.path == '/baseball'
    
def test_anvil_status(app, client):
    res=client.get('/anvil')
    assert res.status_code == 200

def test_anvil_path(app, client):
    url = '/anvil'
    res = client.get(url)
    assert res.request.path == '/anvil'

def test_book_status(app, client):
    res=client.get('/book')
    assert res.status_code == 200

def test_book_path(app, client):
    url = '/book'
    res = client.get(url)
    assert res.request.path == '/book'

def test_drums_status(app, client):
    res=client.get('/drums')
    assert res.status_code == 200

def test_drums_path(app, client):
    url = '/drums'
    res = client.get(url)
    assert res.request.path == '/drums'
    
def test_dumbbell_status(app, client):
    res=client.get('/dumbbell')
    assert res.status_code == 200
    
def test_dumbbell_path(app, client):
    url = '/dumbbell'
    res = client.get(url)
    assert res.request.path == '/dumbbell'
    
def test_eyeglasses_status(app, client):
    res=client.get('/eyeglasses')
    assert res.status_code == 200

def test_eyeglasses_path(app, client):
    url = '/eyeglasses'
    res = client.get(url)
    assert res.request.path == '/eyeglasses'

def test_grapes_status(app, client):
    res=client.get('/grapes')
    assert res.status_code == 200

def test_grapes_path(app, client):
    url = '/grapes'
    res = client.get(url)
    assert res.request.path == '/grapes'
    
def test_ladder_status(app, client):
    res=client.get('/ladder')
    assert res.status_code == 200

def test_ladder_path(app, client):
    url = '/ladder'
    res = client.get(url)
    assert res.request.path == '/ladder'

def test_laptop_status(app, client):
    res=client.get('/laptop')
    assert res.status_code == 200

def test_laptop_path(app, client):
    url = '/laptop'
    res = client.get(url)
    assert res.request.path == '/laptop'
    

