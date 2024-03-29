from base_advertising import BaseAdvertising


class Ad(BaseAdvertising):

    list = []

    def __init__(self, object_id, title, img_url, link, advertiser):
        super().__init__(object_id)
        for ad in self.list:
            if ad.object_id == object_id:
                raise Exception("There is an ad with this id!")
        self.title = title
        self.img_url = img_url
        self.link = link
        self.advertiser = advertiser
        Ad.list.append(self)
        advertiser.add_ad(self)

    @staticmethod
    def describe_me():
        return 'Something'
