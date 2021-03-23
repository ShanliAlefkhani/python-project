from base_advertising import BaseAdvertising


class Advertiser(BaseAdvertising):

    def __init__(self, object_id, name):
        super().__init__(object_id)
        self.name = name
