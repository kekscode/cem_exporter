#!/usr/bin/env python3

import requests
import time
import re
from prometheus_client import start_http_server


def fetch_data(url: str):
    """Fetch metrics from HTML frontend"""
    r = requests.get(url)
    return r.content


def extract_metrics(data):
    """Extract metrics to sane format"""
    regex_energy_import_line = re.compile('Energy, Active import<.*')
    regex_energy_import_sum = re.compile('\d+\.\d+')

    data = data.decode('utf-8')

    energy_line = regex_energy_import_line.findall(data)[0]
    energy_line_sum = regex_energy_import_sum.findall(energy_line)[0]

    return energy_line_sum


def transform_metrics():
    """Transform metrics to prometheus compatible format"""
    pass


if __name__ == '__main__':
    start_http_server(9080)
    frontend_url = 'http://localhost:8000/tests/data/stats.html'
    while True:
        data = fetch_data(frontend_url)
        sanitized_data = extract_metrics(data)
        print(sanitized_data)
        time.sleep(1)
