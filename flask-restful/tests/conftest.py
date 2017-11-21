import json
import pytest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


@pytest.fixture
def client(request):
    import restapi.app as rapp
    test_client = rapp.app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client
