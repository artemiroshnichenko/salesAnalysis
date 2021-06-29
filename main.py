import os 
from dotenv import load_dotenv
from processor.connector import ga_connector
from processor.convertor import ga_convertor
from processor.connector import binotel_connector
from processor.convertor import binotel_convertor
from processor.connector import woocommerce_connector
from processor.convertor import woocommerce_convertor
from processor.worker import clickhouse_worker
from datetime import datetime


def ga(dims, metrcs, start_date, end_date, columns):    
    ga_request = ga_connector.GoogleAnaliticsResolver(
        os.getenv('GA_KEY_FILE_LOCATION'), os.getenv('GA_VIEW_ID'))
    ga_request.initialize_analyticsreporting()
    ga_request.request_body(dims, metrcs, start_date, end_date)
    ga_json = ga_request.get_report()
    ga_convert = ga_convertor.GoogleAnaliticsConvertor(ga_json, columns)
    ga_data = ga_convert.get_data()
    clichouse('client', 'browser', ga_data)

def binotel(start_day, end_day):
    binotel_resolv = binotel_connector.BinotelResolver(
        os.getenv('binotel_key'), os.getenv('binotel_secret'))
    binotel_resolv.set_body()
    start_day = int(datetime.timestamp(datetime.strptime(start_day, '%Y-%m-%d')))
    end_day = int(datetime.timestamp(datetime.strptime(end_day, '%Y-%m-%d')))
    data = binotel_resolv.incoming_calls_period(start_day, end_day)
    binotel_convert = binotel_convertor.BinotelConvertor(data)
    in_data = binotel_convert.incoming()
    clichouse('client', 'calls', in_data)
    data = binotel_resolv.calltracking_calls_period(start_day, end_day)
    binotel_convert = binotel_convertor.BinotelConvertor(data)
    in_data = binotel_convert.call_tracking()
    clichouse('client', 'calls', in_data)

def binotel_get(start_day, end_day):
    b = binotel_connector.BinotelResolver(os.getenv('binotel_login'), os.getenv('binotel_pass'))
    html = b.get_call(start_day, end_day)
    binotel_convert = binotel_convertor.BinotelConvertor(html)
    get_data = binotel_convert.get_call()     
    clichouse('client', 'calls', get_data)

def woocommerce():
    woocommerce_resolv = woocommerce_connector.WoocommerceResolver(
        os.getenv('consumer_key'), os.getenv('consumer_secret'))
    data = woocommerce_resolv.get_order()
    woocommerce_convert = woocommerce_convertor.WoocommerceConvertor(data)
    woo_data = woocommerce_convert.get_data_frame()
    clichouse('client', 'client', woo_data)

def woocommerce_form(start_day, end_day):
    start_day = int(datetime.timestamp(datetime.strptime(start_day, '%Y-%m-%d')))
    end_day = int(datetime.timestamp(datetime.strptime(end_day, '%Y-%m-%d')))
    w = woocommerce_connector.WoocommerceResolver(None, os.getenv('form_secret'))
    raw = w.get_form(start_day, end_day)
    c = woocommerce_convertor.WoocommerceConvertor(raw)
    data = c.get_from_form()
    clichouse('client', 'client', data)

def clichouse(database, table, data):
    clickhouse = clickhouse_worker.ClickHouseResolver()
    clickhouse.connect_to_client(host=os.getenv('click_host'), 
                    port=os.getenv('click_port'), database=database)
    clickhouse.insert(table, data)
    clickhouse.disconnect()


def main():
    load_dotenv('configuration/config.env')
    dims = ['ga:dimension2', 'ga:dateHourMinute', 
        'ga:source', 'ga:medium', 'ga:campaign','ga:country', 'ga:sessionCount']
    metrics = ['ga:avgSessionDuration']
    columns = ['ga_id', 'timestamp', 'source', 'medium', 'campaign', 'country', 'session_count','avg_session_duration']
    ga(dims, metrics, '2021-05-01', '2021-06-24', columns)
    dims = ['ga:dimension2', 'ga:dimension1', 'ga:dateHourMinute', 
        'ga:source', 'ga:medium', 'ga:campaign','ga:country', 'ga:sessionCount']
    columns = ['ga_id', 'fb_id', 'timestamp', 'source', 'medium', 'campaign', 'country', 'session_count','avg_session_duration']
    ga(dims, metrics, '2021-06-25', 'today', columns)
    binotel('2020-05-01', '2021-06-26')
    binotel_get('2020-05-01', '2021-06-26')
    woocommerce()
    woocommerce_form('2020-05-01', '2021-06-29')

if __name__ == '__main__':
    main()