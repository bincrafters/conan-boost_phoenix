#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostPhoenixConan(base.BoostBaseConan):
    name = "boost_phoenix"
    url = "https://github.com/bincrafters/conan-boost_phoenix"
    lib_short_names = ["phoenix"]
    header_only_libs = ["phoenix"]
    b2_requires = [
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_core",
        "boost_function",
        "boost_fusion",
        "boost_mpl",
        "boost_predef",
        "boost_preprocessor",
        "boost_proto",
        "boost_range",
        "boost_smart_ptr",
        "boost_type_traits",
        "boost_utility"
    ]
