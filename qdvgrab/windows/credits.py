#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# credits.py - A Credit screen for QDvgrab
# Copyright (c) 2014-2016-2019-2020 Olivier Girard <olivier@openshot.org>
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

# Need for display gui
from PyQt5.QtWidgets import QDialog

# Used for call ui files
from ui.creditsui import Ui_creditscreen

# name of all contributors to the project
OG = {'name': 'Olivier Girard', 'email': 'olivier@openshot.org'}

# credits
CREDITS = {
    'code': [OG, ],
    'documentation': [OG, ],
    'translation': [OG, ],
}


class Credits(QDialog):

    """
    This screen shows who has developed,documented, translated and the licence of the project

    """

    def __init__(self, *args, **kwargs):
        super(Credits, self).__init__(*args, **kwargs)
        self.setupUi()

        self.showLicense()
        self.showAuthors()
        self.showDocumenters()
        self.showTranslators()

    # ==================================================================================================================
    def setupUi(self):

        self.ui = Ui_creditscreen()
        self.ui.setupUi(self)

    # ==================================================================================================================
    def showAuthors(self):

        # init authors
        authors = []
        for person in CREDITS['code']:
            name = person['name']
            email = person['email']
            authors.append("{} - <{}>".format(name, email))
        self.ui.textBrowserwritten.append(str(authors))
 
    def showDocumenters(self):

        # init documenters
        authors = []
        for person in CREDITS['documentation']:
            name = person['name']
            email = person['email']
            authors.append("{} - <{}>".format(name, email))
        self.ui.textBrowserdocumented.append(str(authors))

    def showTranslators(self):

        # init translator
        authors = []
        for person in CREDITS['translation']:
            name = person['name']
            email = person['email']
            authors.append("{} - <{}>".format(name, email))
        self.ui.textBrowsertranslated.append(str(authors))

    # ==================================================================================================================
    def showLicense(self):
        """Display the license"""

        with open('../LICENSE', 'r') as my_licence:
            text = my_licence.read()
            self.ui.textBrowserlicense.setPlainText(text)

