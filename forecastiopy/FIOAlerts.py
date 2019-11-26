# -*- coding: utf-8 -*-
"""
This module recieves an ForecastIO object and holds the alerts weather
conditions. It has one class for this purpose.
"""


class FIOAlerts(object):
    """
    This class recieves an ForecastIO object and holds the alerts weather
    conditions. It has one class for this purpose.
    """
    alerts = None

    def __init__(self, forecast_io):
        """
        Recieves an ForecastIO object and gets the alerts weather conditions
        if they are available in the object.
        """
        if forecast_io.has_alerts():
            self.alerts = forecast_io.get_alerts()

    def get(self, alert=None):
        """
        Returns a dictionary with alert weather conditions.
        Returns None is none are available.
        A day can be passed as an argument, is so function will call get_alert()
        to return that day.
        Look on function get_alert()
        """
        if alert is None:
            return self.alerts
        else:
            return self.get_alert(alert)

    def get_alert(self, alert):
        """
        Recieves a day as an argument and returns the prediction for that alert
        if is available. If not, function will return None.
        """
        if alert > self.alerts_count() or self.alerts_count() is None:
            return None
        else:
            return self.get()[alert-1]

    def alerts_count(self):
        """
        Returns how many alerts of prediction are available.
        Returns None if none is available
        """
        if self.get() is None:
            return None
        else:
            return len(self.get())
