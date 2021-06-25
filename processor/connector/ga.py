from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class GoogleAnaliticsResolver():

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
                'pageSize': 1000
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
        report = self.report
        while True:
            if 'nextPageToken' in report['reports'][0]:
                self.requests_list[0]['pageToken'] = report['reports'][0]['nextPageToken']
                report = self.analytics.reports().batchGet(body=\
                    {'reportRequests':self.requests_list}).execute()
                for element in report['reports'][0]['data']['rows']:
                    self.report['reports'][0]['data']['rows'].append(element)
            else:
                break
        if 'nextPageToken' in self.report['reports'][0]:
            self.report['reports'][0].pop('nextPageToken')
        return self.report


def main():
    pass

if __name__ == '__main__':
    main()