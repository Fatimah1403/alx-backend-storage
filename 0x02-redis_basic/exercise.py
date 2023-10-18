#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method, store an instance of
the Redis client as a private variable named _redis (using redis.Redis()) and
flush the instance using flushdb.Create a store method that takes a data
argument and returns a string. The method should generate a random key
(e.g. using uuid), store the input data in Redis using the
random key and return the key.
Type-annotate store correctly. Remember that data
can be a str, bytes, int or float.

"""
from uuid import uuid4
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Type-annotate store correctly. Remember
    that data can be a str, bytes, int or float.
    """
    def __init__(self):
        """
        initialize a cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store a value in redis
        """
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> UnionOfTypes:
        """
        Retrieve data from Redis and convert it to a desirable format
        """
        data = self._redis.get(key)

        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        automatically parametrize Cache.get with the correct
        conversion function
        """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        automatically parametrize Cache.get with the correct
        conversion function
        """
        return self.get(key, lambda x: int(x))
