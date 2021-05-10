import os 
import mysql.connector as sql
from dotenv import load_dotenv


# Google Analytics Reporting API V4
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


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

    def get_report(self, body):
        """Queries the Analytics Reporting API V4.

        Args:
            analytics: An authorized Analytics Reporting API V4 service object.
            body: Parameters for the report
        Returns:
            The Analytics Reporting API V4 response.
        """
        self.analytics.reports().batchGet(body=body).execute()


def main():
    pass


if __name__ == '__main__':
    main()