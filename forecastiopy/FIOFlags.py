# -*- coding: utf-8 -*-
"""
This module recieves an ForecastIO object and holds the falgs weather
data. It has one class for this purpose.
"""


class FIOFlags(object):
    """
    This class recieves an ForecastIO object and holds the flags weather
    data. It has one class for this purpose.
    """

    flags = None

    def __init__(self, forecast_io):
        """
        Recieves an ForecastIO object and gets the flags weather data
        if they are available in the object.
        """
        if forecast_io.has_flags():
            self.flags = forecast_io.get_flags()
            for item in self.flags.keys():
                setattr(self, item, self.flags[item])

    def get(self):
        """
        Returns a dictionary with flags weather data
        """
        return self.flags

    def available_flags(self):
        """
        Returns the available flags available in weather data
        """
        return self.get().keys()
