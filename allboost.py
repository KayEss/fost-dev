# -*- coding: utf-8 -*-
from configuration import *


for v in range(59, 65):
    if v not in BOOST_VERSIONS and v != 60:
        BOOST_VERSIONS.append(v)
