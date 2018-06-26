"""
adjusty , A Simplified Python Implementation of Adjust API for KPI service
~~~~~~~~~~~~~~~~~~~~~
usage:

   >>> from adjusty.adjust_api import Adjust
   >>> adjust = Adjust()
   >>> adjust.app_token = "abcd"  # For multiple use a list [asbd, sdkdkf]
   >>> adjust.user_token = "ewyurey"
   >>> adjust.set_params(start_date="2018-06-10", end_date="2018-06-11", countries=['in'],kpis=["sessions"],group=["network"], kwargs={"utc_offset": "+05:30", "period": "week"})
   >>> adjust.fetch_cohorts()
   >>> {'result_parameters': {'end_date': '2018-06-11', 'period': 'week', 'start_date': '2018-06-10', 'attribution_type': 'click', 'grouping': ['network', 'periods'], 'attribution_source': 'dynamic', 'countries': ['in'], 'sandbox': False, 'day_def': '24h', 'utc_offset': '+05:30', 'kpis': ['sessions']}, 'result_set':{'token': 'abcd1234', 'networks': [{'token': 'abcd1234', 'name': 'Organic', 'periods': [{'period': '0', 'kpi_values': [00000]}, {'period': '1', 'kpi_values': [0000]}, {'period': '2', 'kpi_values': [000]}]}, {'token': 'abcd', 'name': 'SMS', 'periods': [{'period': '0', 'kpi_values': [0000]} 

:copyright: (c) 2018 by Ashish Srivastava @techieashish.
"""

__title__ = 'adjust_api'
__version__ = '1.1'
__author__ = 'Ashish Srivastava @techieashish'
__copyright__ = 'Copyright 2018 Ashish Srivastava @techieashish'

import requests


class Adjust:

    start_date = None
    end_date = None
    kpis = None
    countries = None
    group = None
    extras = None

    def __init__(self, app_token=None, user_token=None):
        self.app_token = app_token
        self.user_token = user_token

    def set_params(self, start_date: str = "YYYY-MM-DD", end_date: str = "YYYY-MM-DD", countries:
                   list = None, kpis: list = None, group: list = None, kwargs: dict = None):

        """
                :param start_date: str
                :param end_date: str
                :param countries: list
                :param kpis: list
                :param group: list
                :param extras: dict
                :return: None

                """
        for var in [countries, kpis, group]:
            if not isinstance(var, list):
                raise TypeError("{} must be a {}".format(var, list))
        for var in [start_date, end_date]:
            if not isinstance(var, str):
                raise TypeError("{} must be a {}".format(var, str))
        if kwargs is not None and not isinstance(kwargs, dict):
            raise TypeError("{} must be a {}".format(kwargs, dict))
        self.start_date = start_date
        self.end_date = end_date
        self.kpis = kpis
        self.group = group
        self.countries = countries
        self.extras = kwargs

    def get_params(self):
        if self.app_token is list:
            url = "https://api.adjust.com/kpis/v1/" + ",".join(self.app_token)
        else:
            url = "https://api.adjust.com/kpis/v1/" + self.app_token
        params = {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "kpis": ",".join(self.kpis),
            "countries": ",".join(self.countries),
            "user_token": self.user_token,
            "grouping": ",".join(self.group)
        }
        if self.extras is not None:
            for key, val in self.extras.items():
                params[key] = val

        return url, params

    def fetch_deliverables(self):
        url, params = self.get_params()
        response = requests.get(url, params=params)
        return response.json()

    def fetch_events(self):
        base_url, params = self.get_params()
        url = base_url + "/events"
        response = requests.get(url, params=params)
        return response.json()

    def fetch_cohorts(self):
        base_url, params = self.get_params()
        url = base_url + "/cohorts"
        response = requests.get(url, params=params)
        return response.json()
