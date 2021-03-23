from base_advertising import BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, object_id, title, img_url, link, advertiser):
        super().__init__(object_id)
        self.title = title
        self.img_url = img_url
        self.link = link
        self.advertiser = advertiser
