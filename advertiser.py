from base_advertising import BaseAdvertising


class Advertiser(BaseAdvertising):

    list = []
    total_clicks = 0

    def __init__(self, object_id, name):
        super().__init__(object_id)
        for advertiser in self.list:
            if advertiser.object_id == object_id:
                raise Exception("There is an advertiser with this id!")
        self.name = name
        Advertiser.list.append(self)
        self.ads = []

    @staticmethod
    def help():
        return 'Something'

    @staticmethod
    def describe_me():
        return 'Something'

    def inc_clicks(self):
        super().inc_clicks()
        Advertiser.total_clicks += 1

    def add_ad(self, ad):
        if ad not in self.ads:
            self.ads.append(ad)
