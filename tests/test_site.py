import os

def test_site_has_correct_text():
    fp = open(os.path.join(os.path.dirname(__file__), '../playbooks/site/index.html'))
    contents = fp.read()

    assert 'Sebastian' in contents