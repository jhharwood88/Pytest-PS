import pytest

from phonebook import Phonebook

#pytest has a good amount of detail built in with the assertion testing, showing specifically where the test failed and how it failed. It has good reporting for test failures that make it much easier to interpret tests. Pycharm has a built in test runner for testing to be able to automate testing arguments rather than manually calling them from the terminal. There are aditional information sources available through pycharm.

@pytest.fixture
def phonebook(tmpdir):
    "Provides an empty Phonebook"
    return Phonebook(tmpdir)


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")


