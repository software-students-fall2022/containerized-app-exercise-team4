import json


def test_index_status(app, client):
    res = client.get('/')
    assert res.status_code == 200


def test_index_path(app, client):
    url = '/'
    res = client.get(url)
    assert res.request.path == '/'


def test_leaderboard_status(app, client):
    res = client.get('/leaderboard')
    assert res.status_code == 200


def test_leaderboard_path(app, client):
    url = '/leaderboard'
    res = client.get(url)
    assert res.request.path == '/leaderboard'


def test_active_status(app, client):
    res = client.get('/active')
    assert res.status_code == 200


def test_active_path(app, client):
    url = '/active'
    res = client.get(url)
    assert res.request.path == '/active'


def test_statistics_status(app, client):
    res = client.get('/statistics')
    assert res.status_code == 200


def test_statistics_path(app, client):
    url = '/statistics'
    res = client.get(url)
    assert res.request.path == '/statistics'


def test_baseball_status(app, client):
    res = client.get('/baseball')
    assert res.status_code == 200


def test_baseball_path(app, client):
    url = '/baseball'
    res = client.get(url)
    assert res.request.path == '/baseball'


def test_anvil_status(app, client):
    res = client.get('/anvil')
    assert res.status_code == 200


def test_anvil_path(app, client):
    url = '/anvil'
    res = client.get(url)
    assert res.request.path == '/anvil'


def test_book_status(app, client):
    res = client.get('/book')
    assert res.status_code == 200


def test_book_path(app, client):
    url = '/book'
    res = client.get(url)
    assert res.request.path == '/book'


def test_drums_status(app, client):
    res = client.get('/drums')
    assert res.status_code == 200


def test_drums_path(app, client):
    url = '/drums'
    res = client.get(url)
    assert res.request.path == '/drums'


def test_dumbbell_status(app, client):
    res = client.get('/dumbbell')
    assert res.status_code == 200


def test_dumbbell_path(app, client):
    url = '/dumbbell'
    res = client.get(url)
    assert res.request.path == '/dumbbell'


def test_eyeglasses_status(app, client):
    res = client.get('/eyeglasses')
    assert res.status_code == 200


def test_eyeglasses_path(app, client):
    url = '/eyeglasses'
    res = client.get(url)
    assert res.request.path == '/eyeglasses'


def test_grapes_status(app, client):
    res = client.get('/grapes')
    assert res.status_code == 200


def test_grapes_path(app, client):
    url = '/grapes'
    res = client.get(url)
    assert res.request.path == '/grapes'


def test_ladder_status(app, client):
    res = client.get('/ladder')
    assert res.status_code == 200


def test_ladder_path(app, client):
    url = '/ladder'
    res = client.get(url)
    assert res.request.path == '/ladder'


def test_laptop_status(app, client):
    res = client.get('/laptop')
    assert res.status_code == 200


def test_laptop_path(app, client):
    url = '/laptop'
    res = client.get(url)
    assert res.request.path == '/laptop'


def test_sun_status(app, client):
    res = client.get('/sun')
    assert res.status_code == 200


def test_sun_path(app, client):
    url = '/sun'
    res = client.get(url)
    assert res.request.path == '/sun'


def test_index_page_heading(app, client):
    url = '/'
    res = client.get(url)
    assert b'Welcome to the Game Dashboard' in res.data


def test_index_page_links(app, client):
    url = '/'
    res = client.get(url)
    assert b'Leaderboard' in res.data
    assert b'Most active users' in res.data
    assert b'Object comparisons' in res.data
    assert b'Individual object statistics' in res.data


def test_leaderboard_heading(app, client):
    url = '/leaderboard'
    res = client.get(url)
    assert b'Leaderboard' in res.data


def test_active_heading(app, client):
    url = '/active'
    res = client.get(url)
    assert b'Most active users' in res.data


def test_comparison_heading(app, client):
    url = '/comparison'
    res = client.get(url)
    assert b'Object Comparisons' in res.data


def test_statistics_heading(app, client):
    url = '/statistics'
    res = client.get(url)
    assert b'Select an Object to View its Statistics' in res.data


def test_statistics_links(app, client):
    url = '/statistics'
    res = client.get(url)
    assert b'Baseball Bat' in res.data
    assert b'Eyeglasses' in res.data
    assert b'Grapes' in res.data
    assert b'Anvil' in res.data
    assert b'Laptop' in res.data
    assert b'Dumbbell' in res.data
    assert b'Sun' in res.data
    assert b'Book' in res.data
    assert b'Drums' in res.data
    assert b'Ladder' in res.data


def test_baseball_page(app, client):
    url = '/baseball'
    res = client.get(url)
    assert b'Baseball Bat' in res.data


def test_eyeglasses_page(app, client):
    url = '/eyeglasses'
    res = client.get(url)
    assert b'Eyeglasses' in res.data


def test_grapes_page(app, client):
    url = '/grapes'
    res = client.get(url)
    assert b'Grapes' in res.data


def test_anvil_page(app, client):
    url = '/anvil'
    res = client.get(url)
    assert b'Anvil' in res.data


def test_laptop_page(app, client):
    url = '/laptop'
    res = client.get(url)
    assert b'Laptop' in res.data


def test_dumbbell_page(app, client):
    url = '/dumbbell'
    res = client.get(url)
    assert b'Dumbbell' in res.data


def test_anvil_page(app, client):
    url = '/anvil'
    res = client.get(url)
    assert b'Anvil' in res.data


def test_book_page(app, client):
    url = '/book'
    res = client.get(url)
    assert b'Book' in res.data


def test_drums_page(app, client):
    url = '/drums'
    res = client.get(url)
    assert b'Drums' in res.data


def test_ladder_page(app, client):
    url = '/ladder'
    res = client.get(url)
    assert b'Ladder' in res.data
