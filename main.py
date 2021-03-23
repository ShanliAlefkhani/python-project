from base_advertising import BaseAdvertising
from advertiser import Advertiser
from ad import Ad

try:
    advertiser1 = Advertiser(1, 'name1')
    advertiser2 = Advertiser(2, "name2")
    ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
    ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)
    print(BaseAdvertising.describe_me())
    print(Ad.describe_me())
    print(Advertiser.describe_me())
    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad2.inc_views()
    ad1.inc_clicks()
    ad1.inc_clicks()
    ad2.inc_clicks()
    print(advertiser2.name)
    advertiser2.name = 'new name'
    print(advertiser2.name)
    print(ad1.clicks)
    print(advertiser2.clicks)
    print(Advertiser.total_clicks)
    print(Advertiser.help())
except Exception as e:
    print(e.args[0])
