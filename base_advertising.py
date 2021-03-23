class BaseAdvertising:

    clicks = 0
    views = 0

    def __init__(self, object_id):
        self.object_id = object_id

    @staticmethod
    def describe_me():
        return 'Something'

    def inc_clicks(self):
        self.clicks += 1

    def inc_views(self):
        self.views += 1
