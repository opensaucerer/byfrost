#!/usr/bin/env python3

from bifrost import BifrostError


def test_error_struct():
    try:
        raise BifrostError("some stuff", "test")
    except BifrostError as e:
        assert e.code() == "test"
        assert e.Error == "some stuff"
