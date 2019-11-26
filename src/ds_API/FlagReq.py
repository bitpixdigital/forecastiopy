class FlagReq(object):
    flags = None

    def __init__(self, weather_req):
        if weather_req.has_flags():
            self.flags = weather_req.gFlags()
            for item in self.flags.keys():
                setattr(self, item, self.flags[item])

    def get(self):
        return self.flags

    def available_flags(self):
        return self.get().keys()