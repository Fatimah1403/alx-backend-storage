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
from functools import wraps
from typing import Union, Callable, Optional

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    '''Tracks the number of calls made to a method in a Cache class.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Invokes the given method after incrementing its call counter.
        '''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


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
        Retrieves data stored in redis using a key
        converts the result/value back to the desired format
        """
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, value: str) -> str:
        """ get a string """
        return self.get(self._key, str)

    def get_int(self, value: str) -> int:
        """ get an int """
        return self.get(self._key, int)
