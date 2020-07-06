import json
import pytest
import selenium.webdriver
import os

@pytest.fixture
def config(scope='session'):
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print("Files in %r: %s" % (cwd, files))
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ["Firefox","Chrome"]
    assert isinstance(config['implicit_wait'], int)
    assert config ['implicit_wait']>0

    return config

@pytest.fixture
def browser(config):
    if config['browser']=='Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser']== 'Chrome':
        b = selenium.webdriver.Chrome()
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    b.implicitly_wait(config['implicit_wait'])

    yield b
    b.quit()
