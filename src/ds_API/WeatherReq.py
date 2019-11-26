import json
import requests
import sys


class WeatherReq(object):
    '''
    Class Purpose:
    Handles connection, builds the Darksky URL, and gets the overall data from the API.
    '''
    # Initialisation attributes
    ds_URL = 'https://api.darksky.net/forecast/'
    apiKey = None
    units_url = None
    time_url = None
    extend_url = None
    exclude_url = None
    lang_url = None
    extend = None
    cache_control = None
    expires = None
    x_forecast_api_calls = None
    response_time = None
    raw_response = None

    # json objects within darksky api
    currently = None
    minutely = None
    hourly = None
    daily = None
    flags = None
    alerts = None

    # Languages
    lang_en = 'en'
    lang_es = 'es'
    lang_fr = 'fr'
    lang_it = 'it'
    lang_ru = 'ru'
    # Units used by country
    units_uk = 'uk'
    units_us = 'us'
    units_si = 'si'
    units_ca = 'ca'
    units_auto = 'auto'
    allowed_excludes_extends = ('currently', 'minutely', 'hourly',
                                'daily', 'alerts', 'flags')

    def __init__(self, apiKey, extend=None, exclude_url=None, units_url=units_uk, lang_url=lang_en,
                 latitude=None, longitude=None, time_url=None):
        if apiKey.__len__() == 32:
            self.apiKey = apiKey
            self.longitude = longitude
            self.latitude = latitude
            self.exclude_url = exclude_url
            self.units_url = units_url
            self.time_url = time_url
            self.lang_url = lang_url
            if latitude is not None and longitude is not None:
                self.getForecast(latitude, longitude)
            else:
                print('Latitude or longitude not set')
        else:
            print('The API Key is invalid.')

    def buildUrl(self, longitude, latitude):
        try:
            float(longitude)
            float(latitude)
        except ValueError:
            raise ValueError('Longitude and Latitude values both must be a float number.')
        url = self.ds_URL + self.apiKey + '/'
        url += str(latitude).strip() + ',' + str(longitude).strip()
        if self.time_url and not self.time_url.isspace():
            url += ',' + self.time_url.strip()
        url += '?units=' + self.units_url.strip()
        url += '&lang=' + self.lang_url.strip()
        if self.exclude_url is not None:
            excludes = ''
            for item in self.exclude_url:
                if item in self.allowed_excludes_extends:
                    excludes += item + ','
            if excludes.__len__() > 0:
                url += '&exclude=' + excludes.rstrip(',')
        if self.extend_url is not None:
            extends = ''
            for item in self.extend_url:
                if item in self.allowed_excludes_extends:
                    extends += item + ','
            if extends.__len__() > 0:
                url += '&extend=' + extends.rstrip(',')
        return url

    def getForecast(self, latitude, longitude):
        reply = self.HTTP(self.buildUrl(latitude, longitude))
        self.forecast = json.loads(reply)
        for item in self.forecast.keys():
            setattr(self, item, self.forecast[item])

    def getUrl(self):
        return self.buildUrl(self.longitude, self.latitude)

    def HTTP(self, req_url):
        try:
            headers = {'Accept-Encoding': 'gzip, deflate'}
            response = requests.get(req_url, headers=headers)
        except requests.exceptions.Timeout:
            print('Error: Timeout')
        except requests.exceptions.TooManyRedirects:
            print('Error: TooManyRedirects')
        except requests.exceptions.RequestException as ex:
            print(ex)
            sys.exit(1)
        try:
            self.cache_control = response.headers['Cache-Control']
            self.expires = response.headers['Expires']
            self.forecast_api_calls = response.headers['X-Forecast-API-Calls']
            self.response_time = response.headers['X-Response-Time']
        except KeyError as keyErr:
            print(f'Warning: Could not get headers. {keyErr}')
        if response.status_code != 200:
            raise requests.exceptions.HTTPError('Bad response')

        self.raw_response = response.text
        return self.raw_response

    def has_currently(self):
        return 'currently' in self.forecast

    def gCurrently(self):
        if self.has_currently():
            return self.currently
        else:
            return None

    def has_daily(self):
        return 'daily' in self.forecast

    def gDaily(self):
        if self.has_daily():
            return self.daily
        else:
            return None

    def has_hourly(self):
        return 'hourly' in self.forecast

    def gHourly(self):
        if self.has_hourly():
            return self.hourly
        else:
            return None

    def has_minutely(self):
        return 'minutely' in self.forecast

    def gMinutely(self):
        if self.has_minutely():
            return self.minutely
        else:
            return None

    def has_flags(self):
        return 'flags' in self.forecast

    def gFlags(self):
        if self.has_flags():
            return self.flags
        else:
            return None

    def has_alerts(self):
        return 'alerts' in self.forecast

    def gAlerts(self):
        if self.has_alerts():
            return self.alerts
        else:
            return None