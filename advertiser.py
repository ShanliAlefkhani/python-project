from base_advertising import BaseAdvertising


class Advertiser(BaseAdvertising):

    total_clicks = 0

    def __init__(self, object_id, name):
        super().__init__(object_id)
        self.name = name

    @staticmethod
    def help():
        return 'Something'

    @staticmethod
    def describe_me():
        return 'Something'

    def inc_clicks(self):
        super().inc_clicks()
        self.total_clicks += 1
