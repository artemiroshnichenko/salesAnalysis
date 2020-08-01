from urllib import parse

def url_parse(url):
    url = dict(parse.parse_qsl(parse.urlsplit(url).query))
    print(url)

url = 'utm_Field":["||time: 14:56:17&date: 07:01:2020&HTTP_REFERER: https:\/\/pipl.ua\/ru\/kupi-motioncam-i-poluchi-skidku-do-2000-grn-na-hub-2\/?utm_source=youtube&utm_medium=video&utm_campaign=promo||"]||"_ga_tracked":["1"]||"_date_paid":["1578410321"]||"_paid_date":["2020-01-07 15:18:41"]||"_download_permissions_granted":["yes"]||"_recorded_sales":["yes"]||"_recorded_coupon_usage_counts":["yes"]||"_order_stock_reduced":["yes"]||"_edit_lock":["1578410931:1https:\/\/pipl.ua\/ru\/kupi-motioncam-i-poluchi-skidku-do-2000-grn-na-hub-2\/?utm_source=youtube&utm_medium=video&utm_campaign=promo"]}'
url_parse(url)