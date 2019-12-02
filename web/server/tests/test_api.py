import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from aplication import app, routes
from aplication.models import Base, Image


@pytest.fixture()
def test_client():

    app.config['DATABASE'] = app.config['TEST_DATABASE']
    testing_client = app.test_client(use_cookies=True)
    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture()
def init_database():
    engine = create_engine(app.config['DATABASE'])
    Base.metadata.create_all(engine)
    row = Image(id=1, path='data/images/photo.jpg', result=None, out_path=None)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(row)
    session.commit()
    session.close()

    yield init_database
    Base.metadata.drop_all(engine)


def test_get_result(test_client, init_database):
    resp = test_client.get('/photos/1/')
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data['expression'] == 'x^q + 2x + 5'
