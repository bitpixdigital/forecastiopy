# -*- coding: utf-8 -*-
"""
This module recieves an ForecastIO object and holds the hourly weather
conditions. It has one class for this purpose.
"""


class FIOHourly(object):
    """
    This class recieves an ForecastIO object and holds the hourly weather
    conditions. It has one class for this purpose.
    """

    hourly = None

    def __init__(self, forecast_io):
        """
        Recieves an ForecastIO object and gets the hourly weather conditions
        if they are available in the object.
        """
        if forecast_io.has_hourly():
            self.hourly = forecast_io.get_hourly()
            for item in forecast_io.get_hourly().keys():
                setattr(self, item, forecast_io.get_hourly()[item])
            for hour in range(0, self.hours()):
                for item in self.get_hour(hour).keys():
                    setattr(self, 'hour_'+str(hour+1)+'_'+item, \
                    self.get_hour(hour)[item])

    def get(self, hour=None):
        """
        Returns a dictionary with hourly weather conditions.
        Returns None is none are available.
        A day can be passed as an argument, is so function will call get_hour()
        to return that day.
        Look on function get_hour()
        """
        if hour is None:
            return self.hourly
        else:
            return self.get_hour(hour)

    def get_hour(self, hour):
        """
        Recieves a hour as an argument and returns the prediction for that hour
        if is available. If not, function will return None.
        """
        if hour > self.hours():
            return None
        else:
            return self.get()['data'][hour-1]

    def hours(self):
        """
        Returns how many hours of prediction are available
        """
        return len(self.get()['data'])
