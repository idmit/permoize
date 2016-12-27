# -*- coding: utf-8 -*-

import pytest

from permoize.core import takeoff

def test_takeoff():
    assert takeoff() == 'Takeoff complete!'
