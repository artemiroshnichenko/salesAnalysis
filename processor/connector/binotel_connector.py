from datetime import datetime
import requests
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

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
    
    def get_call(self, start_day, end_day):
        start_day = datetime.strftime(datetime.strptime(start_day, '%Y-%m-%d'), '%d.%m.%Y')
        end_day = datetime.strftime(datetime.strptime(end_day, '%Y-%m-%d'), '%d.%m.%Y')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('window-size=1920x935')
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                    options=chrome_options)
        self.login(self.key, self.secret, start_day, end_day)
        return self.driver.page_source
        
    def login(self, login, passw, start_day, end_day):
        url = 'https://my.binotel.ua/?module=gcStatistics&showOnlyFilters=&startDate='\
             + start_day + '&stopDate=' + end_day
        self.driver.get(url)
        sleep(2)
        try: 
            logining = self.driver.find_element_by_name('logining[email]')
            password = self.driver.find_element_by_name('logining[password]')
            button = self.driver.find_element_by_name('logining[submit]')
            logining.send_keys(login)
            password.send_keys(passw)
            button.click()
            sleep(10)
            self.driver.get('https://my.binotel.ua/?module=gcStatistics&\
                showOnlyFilters=&startDate=%s&stopDate=%s' % start_day, end_day)
        except:
            pass
        return self.driver
    

def main():
    pass

if __name__ == '__main__':
    main()