#!/usr/bin/env python3
"""
 a Python function that lists all documents in a collection:
 Return an empty list if no document in the collection
"""


def list_all(mongo_collection):
    """
    Return an empty list if no document in the collection
    """
    if not mongo_collection:
        return []
    cursor = mongo_collection.find()
    return [i for i in cursor]
