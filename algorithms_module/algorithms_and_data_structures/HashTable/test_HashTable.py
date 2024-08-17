import pytest
from algorithms_module.algorithms_and_data_structures.HashTable.HashTable import HashTable

@pytest.fixture
def hash_table():
    ht = HashTable(size=10)
    ht.add('key1', 'value1')
    ht.add('key2', 'value2')
    return ht

@pytest.mark.parametrize('expected_table',
                         [
                             ({'key1': 'value1'}),
                             ({'key2': 'value2'})
                         ])

def test_add(hash_table, expected_table):
    for k, v in expected_table.items():
        assert hash_table.get(k) == v

@pytest.mark.parametrize('key, expected_value',
                         [
                             ('key1', 'value1'),
                             ('key2', 'value2')
                         ])

def test_get(hash_table, key, expected_value):
    assert hash_table.get(key) == expected_value

@pytest.mark.parametrize('key, expected_result',
                         [
                             ('key1', pytest.raises(KeyError)),
                             ('key2', pytest.raises(KeyError))
                         ])

def test_delete(hash_table, key, expected_result):
    hash_table.delete(key)
    with expected_result:
        assert hash_table.get(key) == expected_result