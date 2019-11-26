# -*- coding: utf-8 -*-
"""
This module recieves an ForecastIO object and holds the minutely weather
conditions. It has one class for this purpose.
"""

class FIOMinutely(object):
    """
    This class recieves an ForecastIO object and holds the minutely weather
    conditions. It has one class for this purpose.
    """

    minutely = None

    def __init__(self, forecast_io):
        """
        Recieves an ForecastIO object and gets the minutely weather conditions
        if they are available in the object.
        """
        if forecast_io.has_minutely():
            self.minutely = forecast_io.get_minutely()
            for item in forecast_io.get_minutely().keys():
                setattr(self, item, forecast_io.get_minutely()[item])
            for minute in range(0, self.minutes()):
                for item in self.get_minute(minute).keys():
                    setattr(self, 'minute_'+str(minute+1)+'_'+item, \
                    self.get_minute(minute)[item])

    def get(self, minute=None):
        """
        Returns a dictionary with minutely weather conditions.
        Returns None is none are available.
        A day can be passed as an argument, is so function will call get_minute()
        to return that day.
        Look on function get_minute()
        """
        if minute is None:
            return self.minutely
        else:
            return self.get_minute(minute)

    def get_minute(self, minute):
        """
        Recieves a minute as an argument and returns the prediction for that
        minute if is available. If not, function will return None.
        """
        if minute > self.minutes():
            return None
        else:
            return self.get()['data'][minute-1]

    def minutes(self):
        """
        Returns how many minutes of prediction are available
        """
        return len(self.get()['data'])
