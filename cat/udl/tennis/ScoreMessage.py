import gettext
import locale
import os
from gettext import gettext as _

import sys

appdir = os.path.dirname(sys.argv[0])
appdir = os.path.abspath(appdir)
localedir = os.path.join(appdir, "locales")

gettext.install('bundle', localedir, "utf-8")


class ScoreMessage(object):
    LOVE_ALL = _("Love-All")
    FIFTEEN_ALL = _("Fifteen-All")
    THIRTY_ALL = _("Thirty-All")
    DEUCE = _("Deuce")

    ADVANTAGE = _("Advantage ")
    WIN_FOR = _("Win for ")

    LOVE = _("Love")
    FIFTEEN = _("Fifteen")
    THIRTY = _("Thirty")
    FORTY = _("Forty")
