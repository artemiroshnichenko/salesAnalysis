from datetime import datetime
import requests


class BinotelResolver():

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.API_URLS = {
        'calltracking': 'https://api.binotel.com/api/4.0/stats/calltracking-calls-for-period.json',
        'incomming': 'https://api.binotel.com/api/4.0/stats/incoming-calls-for-period.json'
        }
    
    def request_perid(self, name, start_day=datetime.timestamp(datetime.today()),
                            end_day=datetime.timestamp(datetime.today())):
        """Request to get call report
        Args:
            name: type of request
            start_day: timestamp of start period day
            end_day: timestamp of end period day
        Returns:
            json report. 
        """
        api_url = self.API_URLS[name]
        params = {
                'key': self.key,
                'secret': self.secret,
                'startTime': start_day,
                'stopTime': end_day,
            }
        response = requests.post(api_url, json=params)
        if response.status_code == 200: 
            if response.json()['status'] == 'success':
                self.json = response.json()
                return self.json
            else:
                print('Wrong parametrs ', response.json())
        else:
            print('Wrong request ', response)
    
    def get_call():
        #Нужно реализовывать через запрос в браузере
        pass


def main():
    pass

if __name__ == '__main__':
    main()