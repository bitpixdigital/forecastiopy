import src.ds_API.WeatherReq as WeatherReq
import src.ds_API.CurrentReq as CurrentReq


class Run:
    '''
    Class solely for testing out the Darksky API functionality.
    '''
    Belfast = [54.6068577, -5.9363657]
    api = "insert api key here"

    req = WeatherReq.WeatherReq(api, latitude=Belfast[0], longitude=Belfast[1])
    curr = CurrentReq.CurrentReq(req)
    print(f'Temperature: {curr.temperature} degrees')
