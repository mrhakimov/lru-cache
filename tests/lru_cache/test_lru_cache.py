import pytest

from lru_cache import LRUCache


@pytest.fixture
def init_cache():
    return LRUCache(2)


def test_is_empty(init_cache):
    assert init_cache.is_empty()


def test_put(init_cache):
    init_cache.put(1, 1)
    assert init_cache.get(1) == 1

    init_cache.put(2, 2)
    assert init_cache.get(2) == 2

    init_cache.put(2, 3)
    assert init_cache.get(2) == 3

    init_cache.put(3, 3)
    assert init_cache.get(3) == 3

    assert init_cache.get(1) is None


def test_random_puts_and_gets(init_cache):
    init_cache.put(1, 1)
    init_cache.put(2, 2)

    assert init_cache.get(1) == 1

    init_cache.put(3, 3)

    assert init_cache.get(2) is None

    init_cache.put(4, 4)

    assert init_cache.get(1) is None
    assert init_cache.get(3) == 3
    assert init_cache.get(4) == 4

    assert init_cache.get(2) is None

    init_cache.put(2, 6)

    assert init_cache.get(1) is None

    init_cache.put(1, 5)

    init_cache.put(1, 2)

    assert init_cache.get(1) == 2
    assert init_cache.get(2) == 6
