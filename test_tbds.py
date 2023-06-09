from TBDS import TBDS
import os.path
from collections import Counter
import pytest


@pytest.fixture(scope='session')
def setup():
    print("Setting up...")
    tbds = TBDS()

    words = _readWords('words.txt')
    for word in words:
        tbds.add(word, word)

    return tbds, words


def test_createTBDS(setup):
    tbds = setup[0]
    words = setup[1]

    # check all words
    for word in words:
        assert tbds.containsKey(word)

def test_keysAndValues(setup):
    tbds = setup[0]
    words = setup[1]

    for word in words:
        assert tbds.get(word) == word

def test_count(setup):
    tbds = setup[0]
    words = setup[1]
    assert tbds.count() == len(words)

def test_searchPrefix(setup):
    tbds = setup[0]
    words = setup[1]

    # Check the values returned for a number of prefix values
    # Compares the returned result to the true result
    searchPrefixes = ["add", "bril", "cri", "da", "enl", "lor", "mar", "perfection", "rit", "sim", "tra", "una", "ze"]
    for prefix in searchPrefixes:
        realResult = _matchPrefix(prefix, words)
        yourResult = tbds.getKeysForPrefix(prefix)
        print("Result should contain:", realResult)
        print("        Actual result:", yourResult)
        assert Counter(realResult) == Counter(yourResult)



def _matchPrefix(prefix, words) -> list:
    result = []
    for s in words:
        if s.startswith(prefix):
            result.append(s)
    return result

def _readWords(filename: str) -> list:
    if not os.path.isfile(filename):
        raise FileNotFoundError("No such file")

    words = None
    with open(filename) as f:
        words = [line.rstrip('\n') for line in f]

    return words
