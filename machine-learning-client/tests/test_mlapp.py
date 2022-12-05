import json


def test_index_status(app, client):
    res = client.get('/')
    assert res.status_code == 200

def sanity_check(self):
    expected = True
    actual = True
    assert expected == actual

def test_puzzle_status(app, client):
    response = client.get('/puzzle', follow_redirects=True)
    assert response.status_code == 200 
    
def test_draw_status(app, client):
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200

def test_register_status(app, client):
    response = client.get('/register')
    assert response.status_code == 200

def test_login_status(app, client):
    response = client.get('/login')
    assert response.status_code == 200

def test_logout_status(app, client):
    response = client.get('/login')
    assert response.status_code == 200
    
def test_register_name(app,client):
    response = client.get('/register')
    html = response.get_data(as_text=True)
    assert 'name="username"' in html
    
def test_register_password(app,client):
    response = client.get('/register')
    html = response.get_data(as_text=True)
    assert 'name="password"' in html
    
def test_login_name(app,client):
    response = client.get('/login')
    html = response.get_data(as_text=True)
    assert 'name="username"' in html

def test_login_password(app,client):
    response = client.get('/login')
    html = response.get_data(as_text=True)
    assert 'name="password"' in html
    
def test_draw_heading(app,client):
    response = client.get("/draw")
    assert b'Skip' in response.data
    
def test_draw_heading1(app,client):
    response = client.get("/draw")
    assert b'Next' in response.data
    
def test_draw_heading2(app,client):
    response = client.get("/draw")
    assert b'Clear' in response.data
    
def test_draw_heading3(app,client):
    response = client.get("/draw")
    assert b'Quick' in response.data
    
def test_draw_heading4(app,client):
    response = client.get("/draw")
    assert b'Draw' in response.data
    
def test_draw_heading5(app,client):
    response = client.get("/draw")
    assert b'Doodler' in response.data
    
