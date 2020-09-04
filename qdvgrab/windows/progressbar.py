#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# progressbar.py - A pop-up progressbar for QDvgrab
# Copyright (c) 2020 Olivier Girard <olivier@openshot.org>
#
# QDvgrab is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# QDvgrab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys

from PyQt5.QtCore import QObject, pyqtSignal


class WorkersSignals(QObject):

    progress = pyqtSignal(int)
    finished = pyqtSignal()
    cancel = pyqtSignal()
    error = pyqtSignal()
    result = pyqtSignal(str)

    