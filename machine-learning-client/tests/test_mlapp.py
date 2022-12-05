import json


def test_index_status(flask_app):
    res = flask_app.get('/')
    assert res.status_code == 200

def sanity_check(self):
    expected = True
    actual = True
    assert expected == actual

def test_puzzle_status(flask_app):
    response = flask_app.get('/puzzle', follow_redirects=True)
    assert response.status_code == 200 
    
def test_draw_status(flask_app):
    response = flask_app.get('/logout', follow_redirects=True)
    assert response.status_code == 200

def test_register_status(flask_app):
    response = flask_app.get('/register')
    assert response.status_code == 200

def test_login_status(flask_app):
    response = flask_app.get('/login')
    assert response.status_code == 200

def test_logout_status(flask_app):
    response = flask_app.get('/login')
    assert response.status_code == 200
    
def test_register_name(flask_app):
    response = flask_app.get('/register')
    html = response.get_data(as_text=True)
    assert 'name="username"' in html
    
def test_register_password(flask_app):
    response = flask_app.get('/register')
    html = response.get_data(as_text=True)
    assert 'name="password"' in html
    
def test_login_name(flask_app):
    response = flask_app.get('/login')
    html = response.get_data(as_text=True)
    assert 'name="username"' in html

def test_login_password(flask_app):
    response = flask_app.get('/login')
    html = response.get_data(as_text=True)
    assert 'name="password"' in html
    
def test_draw_heading(flask_app):
    response = flask_app.get("/draw")
    assert b'Skip' in response.data
    
def test_draw_heading1(flask_app):
    response = flask_app.get("/draw")
    assert b'Next' in response.data
    
def test_draw_heading2(flask_app):
    response = flask_app.get("/draw")
    assert b'Clear' in response.data
    
def test_draw_heading3(flask_app):
    response = flask_app.get("/draw")
    assert b'Quick' in response.data
    
def test_draw_heading4(flask_app):
    response = flask_app.get("/draw")
    assert b'Draw' in response.data
