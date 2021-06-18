import os 
import mysql.connector as sql
from dotenv import load_dotenv
import pandas as pd
import woocommerce

# Google Analytics Reporting API V4
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import requests
from datetime import datetime, timedelta
import hashlib
import json


class googleAnalitics():

    def __init__(self, KEY_FILE_LOCATION, VIEW_ID):
        self.SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
        self.KEY_FILE_LOCATION = KEY_FILE_LOCATION
        self.VIEW_ID = VIEW_ID

    def initialize_analyticsreporting(self):
        """Initializes an Analytics Reporting API V4 service object.
        Returns:
            An authorized Analytics Reporting API V4 service object.
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.KEY_FILE_LOCATION, self.SCOPES)
        # Build the service object.
        self.analytics = build('analyticsreporting', 'v4', credentials=credentials)

    def request_body(self, DIMS, METRICS, START_DATE='today', END_DATE='today'):
        """Create request list for report
        Args:
            DIMS: List of dimensions
            METRICS: List of metrics
            START_DATE: Start date for report
            END_DATE: End date for report
        Returns:
            Request body
        """
        self.DIMS = DIMS
        self.METRICS = METRICS
        self.requests_list =  [{
                'viewId': self.VIEW_ID,
                'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
                'dimensions': [{'name': name} for name in DIMS],
                'metrics': [{'expression': exp} for exp in METRICS],
                'pageSize': 100000
            }]

    def get_report(self):
        """Queries the Analytics Reporting API V4.
        Args:
            analytics: An authorized Analytics Reporting API V4 service object.
            body: Parameters for the report
        Returns:
            The Analytics Reporting API V4 response json.
        """
        self.report = self.analytics.reports().batchGet(body=\
            {'reportRequests':self.requests_list}).execute()
            
        return self.report

    def convert_to_df(self):
        """Convert json response to pandas data frame
        Returns:
            Report data frame
        """
        data_dic = {f"{i}": [] for i in self.DIMS + self.METRICS}
        for report in self.report.get('reports', []):
            rows = report.get('data', {}).get('rows', [])
            for row in rows:
                for i, key in enumerate(self.DIMS):
                    data_dic[key].append(row.get('dimensions', [])[i])
                dateRangeValues = row.get('metrics', [])
                for values in dateRangeValues:
                    all_values = values.get('values', [])
                    for i, key in enumerate(self.METRICS):
                        data_dic[key].append(all_values[i])
        df = pd.DataFrame(data=data_dic)
        df.columns = [col.split(':')[-1] for col in df.columns]
        return df


class binotel():

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
            else:
                print('Wrong parametrs ', response.json())
        else:
            print('Wrong request ', response)
    
    def get_call():
        #Нужно реализовывать через запрос в браузере
        pass

        
class woocommerce():

    def __init__(self, key, secret):
        self.url = 'https://pipl.ua/wp-json/wc/v3/orders'
        self.consumer_key = key
        self.consumer_secret = secret

    def get_order(self):
        """Request to get order data from woocommerce
        Args:
            consumer_key: API key
            consumer_secret: API secret
        Returns: all orders in json
        """
        params = {
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret
        }
        headers ={
            'user-agent': 'python'
        }
        response = requests.get(self.url, params=params, headers=headers)
        if response.status_code == 200: 
            self.json = response.json()
        else:
            print('Wrong request ', response)

    def get_form(self):
        pass

class sql():
    pass

class oneC():
    
    def __init__(self):
        pass

    def convert_to_df(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()