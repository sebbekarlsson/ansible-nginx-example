import os


def test_site_has_html_tag():
    fp = open(os.path.join(os.path.dirname(__file__), '../playbooks/site/index.html'))
    contents = fp.read()

    assert '<html lang="en">' in contents


def test_site_mentions_my_name():
    fp = open(os.path.join(os.path.dirname(__file__), '../playbooks/site/index.html'))
    contents = fp.read()

    assert 'Sebastian' in contents


def test_site_has_welcome_text():
    fp = open(os.path.join(os.path.dirname(__file__), '../playbooks/site/index.html'))
    contents = fp.read()

    assert 'Welcome' in contents