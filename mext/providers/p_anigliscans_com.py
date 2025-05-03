from mext.bases import MangaStreamBase


class AniGliScans(MangaStreamBase):

    def __init__(self, name, siteUrl):
        self.language = 'en'
        super(AniGliScans, self).__init__(name, siteUrl)
