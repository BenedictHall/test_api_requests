from lib.cat_facts import *
from unittest.mock import Mock

def test_provide_fact():
    requests_mock = Mock()
    response_mock = Mock()
    requests_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"Cats are pretty neat"}
    cat_facts = CatFacts(requests_mock)
    assert cat_facts.provide() == "Cat fact: Cats are pretty neat"