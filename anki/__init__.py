# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import sys, simplejson as _simplejson, httplib2 as _httplib2
if sys.version_info[0] > 2:
    raise Exception("Anki should be run with Python 2")
elif sys.version_info[1] < 5:
    raise Exception("Anki requires Python 2.5+")
elif sys.getfilesystemencoding().lower() in ("ascii", "ansi_x3.4-1968"):
    raise Exception("Anki requires a UTF-8 locale.")
elif _simplejson.__version__ < "1.7.3":
    raise Exception("SimpleJSON must be 1.7.3 or later.")
elif _httplib2.__version__ < "0.7.0":
    raise Exception("Httplib2 must be 0.7.0 or later.")

version = "1.99"
from anki.storage import Collection
