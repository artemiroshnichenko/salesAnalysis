import re
import rw
import pandas as pd
import numpy
import clean_data as cd


def parse(mark, url):
    result = re.search(r'utm_{}: (.+?)(&|$)'.format(mark), url)
    if result:
        return result.group(1)
    return None

url = '||time: 08:25:25&date: 18:06:2020&utm_source: google&utm_medium: cpc&utm_campaign: {campaign}&utm_term: система видеонаблюдения +купить&HTTP_REFERER: https://www.google.com/||;time: 08:25:28&date: 18:06:2020&utm_source: google&utm_medium: cpc&utm_campaign: {campaign}&utm_term: система видеонаблюдения +купить&HTTP_REFERER: https://www.google.com/'
print(parse('source', url))
