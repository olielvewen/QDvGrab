#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# start_app.py - A Start file for running QDvgrab
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
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo

from windows.qdvgrab import QdvGrab

app_name = "QDvGrab"
app_version = "0.22"
app_author = "Olivier Girard"
author_mail = "olivier@openshot.org"

SUPPORTED_LANGUAGES = ['English', 'French']
PATH = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
HOME_PATH = os.path.join(os.path.expanduser("~"))
USER_PATH = os.path.join(HOME_PATH, ".qdvgrab")
# TEMP_PATH = os.path.join(USER_PATH, "Temp")

if __name__ == "__main__":
    application = QApplication(sys.argv)

    # Translate application
    locale = QLocale().system().name()
    qt_path_locale = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator_qt = QTranslator()
    if translator_qt.load("qt_%s" % locale, qt_path_locale):
        application.installTranslator(translator_qt)

    translator_custom = QTranslator()
    if translator_custom.load("qdvgrab.%s" % locale, "translations"):
        application.installTranslator(translator_custom)
    # enNativeLanguage = len(sys.argv) == 1
    # if enNativeLanguage:
    #     locale = QLocale()
    # else:
    #     languageCountry = sys.argv[1]
    # translators = []
    # for prefixQm in ("qdvgrab.", "qt_", "qtbase_"):
    #     translator = QTranslator()
    #     translators.append(translator)
    #     if enNativeLanguage:
    #         translator.load(locale, prefixQm)
    #     else:
    #         translator.load(prefixQm+languageCountry)
    # application.installTranslator(translator)

    window = QdvGrab()
    window.show()
    print("Welcome to QDvGrab {}. \nHope you'll enjoy it. \nPlease report all bugs,"
          "features request and comments at {}\n".format(app_version, author_mail))

    rc = application.exec_()
    sys.exit(rc)
