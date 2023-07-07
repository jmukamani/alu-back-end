#!/usr/bin/python3
"""
    Python script that returns TODO list progress for a given employee Id
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    """
	request user info by employee ID
    """
    request_employee = requests.get(
	'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
