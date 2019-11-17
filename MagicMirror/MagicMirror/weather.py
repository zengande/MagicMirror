import json

class Weather(object):
    """description of class"""
    @staticmethod
    def getWeather(key, location="CN101210113"):
        # https://free-api.heweather.net/s6/weather/now?location=CN101210113&key=7f1494e17bcf4e8f92520f9f23c04b6b
        #fl	体感温度，默认单位：摄氏度	23
        #tmp	温度，默认单位：摄氏度	21
        #cond_code	实况天气状况代码	100
        #cond_txt	实况天气状况描述	晴
        #wind_deg	风向360角度	305
        #wind_dir	风向	西北
        #wind_sc	风力	3-4
        #wind_spd	风速，公里/小时	15
        #hum	相对湿度	40
        #pcpn	降水量	0
        #pres	大气压强	1020
        #vis	能见度，默认单位：公里	10
        #cloud	云量	23

        return json.dumps({"HeWeather6":[{"basic":{"cid":"CN101210113","location":"西湖","parent_city":"杭州","admin_area":"浙江","cnty":"中国","lat":"30.27293396","lon":"120.14737701","tz":"+8.00"},"update":{"loc":"2019-11-17 21:54","utc":"2019-11-17 13:54"},"status":"ok","now":{"cloud":"0","cond_code":"101","cond_txt":"多云","fl":"18","hum":"61","pcpn":"0.0","pres":"1013","tmp":"20","vis":"16","wind_deg":"352","wind_dir":"北风","wind_sc":"3","wind_spd":"16"}}]})