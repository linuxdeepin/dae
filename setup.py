#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2011~2014 Deepin, Inc.
#               2011~2014 Kaisheng Ye
#
# Author:     Kaisheng Ye <kaisheng.ye@gmail.com>
# Maintainer: Kaisheng Ye <kaisheng.ye@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(
    name = 'dae',
    version = '0.1',
    description = 'Deepin desktop application engine',
    long_description = 'Deepin desktop application engine with PyQt Webkit core',
    author = 'iceleaf',
    author_email = 'kaisheng.ye@gmail.com',
    url = 'https://github.com/linuxdeepin/dae/',
    license = 'GPL-3',
    platforms = ['all'],
    packages = ['dae'],
    package_data = {
        "dae": ["init.js"],
    },
)
