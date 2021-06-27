import requests


class WoocommerceResolver():

    def __init__(self, key, secret):
        self.url = 'https://pipl.ua/wp-json/wc/v3/orders'
        self.consumer_key = key
        self.consumer_secret = secret
        self.MAX_ORDER = 100

    def get_order(self, start_day=None, end_day=None):
        """Request to get order data from woocommerce
        Args:
            consumer_key: API key
            consumer_secret: API secret
            start_day: format 2016-06-22T00:00:00 of start period day
            end_day: format 2016-06-22T00:00:00 of end period day
        Returns: all orders in json
        """
        page_number = 1
        self.json = []
        while True:
            params = {
                'consumer_key': self.consumer_key,
                'consumer_secret': self.consumer_secret,
                'per_page': self.MAX_ORDER,
                'after': start_day,
                'before': end_day,
                'per_page': 100,
                'page': page_number
            }
            headers ={
                'user-agent': 'python'
            }
            response = requests.get(self.url, params=params, headers=headers)
            if response.status_code == 200:
                if response.json() != []:
                    self.json.append(response.json())
                else: 
                    break
            else:
                print('Wrong request ', response)
                return response
            page_number += 1
        return self.json

    def get_form(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()