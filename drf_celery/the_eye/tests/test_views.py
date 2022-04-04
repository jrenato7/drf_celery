import json

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


class TestCreateScheduleSuccessApi(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.event_data = {
            "session_id": "8a79cde8-7dda-414b-b4f7-5ff5e4e26991",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.cwtech.dev",
                "path": "/create_event/"
            },
            "timestamp": "2022-04-02 00:00:0.000000"
        }

        self.resp = self.client.post(
            reverse('the_eye:event_save'),
            data=json.dumps(self.event_data),
            content_type='application/json')

    def test_create_schedule(self):
        self.assertEqual(self.resp.status_code, status.HTTP_200_OK)

    def test_response_message(self):
        dic = json.loads(self.resp.content)
        self.assertTrue(dic["success"])
