# adjusty
adjust api written python

# Python client for the Adjust Statistics API

This is an Python client for the [Adjust KPI service](https://docs.adjust.com/en/kpi-service/). It supports all API
functionalities through well documented functions.

## Installation

```bash
pip install adjusty
```

## Usage

```python
from adjusty.adjut_api import Adjust
```

### Setup and Authentication

In order for you to access the KPI Service, you need to authenticate with `user_token`. Your `user_token`, once you supply it, 
will be used throughout the entire  session. Furthermore, you need to provide `app_tokens` for the requests.


```python
adjust = Adjust()
adjust.user_token = "abcd"
adjust.app_token = "abcd123"
```
This library also supports multiple app_tokens in single request. In order to use multiple app_tokens, provide a list of app_tokens 

```python
adjust.app_token = [abcd, efg]
```

## Setting parameters

Once you've setup your user token and app tokens, then each of these calls will produce data for you straight away.

For details on any of those, you should refer to  the KPI service documentation

```python
adjust.set_params(start_date='2015-01-01', end_date='2015-01-10',
        countries=['us', 'de'], kpis=['clicks', 'sessions', 'installs'], grouping=['network'], 
        kwargs={'utc_offset':'+05:30',
        'period':'week'})

```

### Statistics API calls

There are three functions that return KPI data from the API:
```python
    adjust.fetch_deliverables()
    adjust.fetch_events()
    adjust.fetch_cohorts()
```
## Example

```python
   
   >> adjust.fetch_cohorts()
   
   >> {'result_parameters': {'end_date': '2015-01-01', 'period': 'week', 'start_date': '2015-01-10', 'attribution_type': 'click', 'grouping': ['network', 'periods'], 'attribution_source': 'dynamic', 'countries': ['in'], 'sandbox': False, 'day_def': '24h', 'utc_offset': '+05:30', 'kpis': ['sessions']}, 'result_set':{'token': 'abcd1234', 'networks': [{'token': 'abcd1234', 'name': 'Organic', 'periods': [{'period': '0', 'kpi_values': [00000]}, {'period': '1', 'kpi_values': [0000]}, {'period': '2', 'kpi_values': [000]}]}, {'token': 'abcd', 'name': 'SMS', 'periods': [{'period': '0', 'kpi_values': [0000]} 

```
You can issue calls for multiple app tokens at the same time and group for example by group=['app', 'network']. This will return KPI data for the two apps, grouped by the app and all its network trackers.


Contributions and bug reports are only acceptable as GitHub Pull Requests and issues. Thanks!
