from urllib import parse

def url_parse(url):
    url = dict(parse.parse_qsl(parse.urlsplit(url).query))
    print(url['adf'])

url = 'https://pipl.ua/systems/?utm_source=facebook&utm_medium=ads&utm_campaign=Systems%20Sh%20Vid&utm_content=UA%20-%2024-55&ad=vid%202&placement=Facebook_Mobile_Feed'
url_parse(url)