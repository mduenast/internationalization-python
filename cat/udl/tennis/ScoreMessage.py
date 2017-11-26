from gettext import gettext as _, translation

lang_en = translation('bundle', 'locales', languages=['en'])
lang_es = translation('bundle', 'locales', languages=['es'])

lang_es.install()


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
