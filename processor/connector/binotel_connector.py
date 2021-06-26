from datetime import datetime
import requests


class BinotelResolver():

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.API_URL = 'https://api.binotel.com/api/4.0/'
    
    def set_body(self) -> dict:
        self.body = {
            'key': self.key,
            'secret': self.secret
        }
        return self.body

    def set_date(self, start_day, end_day) -> dict:
        body = self.body
        body.update({
            'startTime': start_day,
            'stopTime': end_day
        })
        return body

    def post(self, path: str, body: dict):
        return self.check_status(requests.post(self.API_URL + path, json=body))

    def check_status(self, response):
        if response.status_code == 200: 
            if response.json()['status'] == 'success':
                self.json = response.json()
                return self.json
            else:
                print('Wrong parametrs ', response.json())
        else:
            print('Wrong request ', response)

    def incoming_calls_period(self, start_day=datetime.timestamp(datetime.today()),
                end_day=datetime.timestamp(datetime.today())):
        return self.post('stats/incoming-calls-for-period.json', self.set_date(start_day, end_day))

    def calltracking_calls_period(self, start_day=datetime.timestamp(datetime.today()),
                end_day=datetime.timestamp(datetime.today())):
        return self.post('stats/calltracking-calls-for-period.json', self.set_date(start_day, end_day))
    
    def get_call():
        #Нужно реализовывать через запрос в браузере
        pass


def main():
    pass

if __name__ == '__main__':
    main()