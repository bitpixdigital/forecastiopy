class AlertReq(object):
    alerts = None
    def __init__(self, weather_req):

        if weather_req.has_alerts():
            self.alerts = weather_req.gAlerts()

    def get(self, alert=None):

        if alert is None:
            return self.alerts
        else:
            return self.gAlerts(alert)

    def gAlerts(self, alert):
        if alert > self.alert_cnt() or self.alert_cnt() is None:
            return None
        else:
            return self.get()[alert-1]

    def alert_cnt(self):
        if self.get() is None:
            return None
        else:
            return len(self.get())