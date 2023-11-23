import requests
import json
from django.http import HttpResponse

class ThingsBoard:
    def __init__(self, token):
        self.token = token

    def post_telemetry(self, telemetry):
        url = f'http://127.0.0.1:8089/api/v1/{self.token}/telemetry'

        try:
            response = requests.post(url, json=telemetry)
            response.raise_for_status()
            return HttpResponse({"message": "Sucess"})
        except Exception as e:
            raise HttpResponse({"message": "error", "detail": e.args})
        
   