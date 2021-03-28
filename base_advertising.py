class BaseAdvertising:

    def __init__(self, object_id):
        self.object_id = object_id
        self.clicks = 0
        self.views = 0

    @staticmethod
    def describe_me():
        return 'Something'

    def inc_clicks(self):
        self.clicks += 1

    def inc_views(self):
        self.views += 1
