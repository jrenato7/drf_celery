from django.test import TestCase

from the_eye.tasks import validate_event, SerializerError, InvalidPayload
from the_eye.models import Event, PageView, PageClick, EventForm, Account


class ValidateEventPageViewSuccessTest(TestCase):

    def setUp(self):
        page_view = {
            "session_id": "d66ac88b-f801-4984-953f-5c6b266494a0",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.cwtech.dev",
                "path": "/"
            },
            "timestamp": "2022-04-01 00:00:0.000000"
        }
        validate_event(page_view)

    def test_create_event(self):
        self.assertTrue(Event.objects.exists())

    def test_create_page_view(self):
        self.assertTrue(PageView.objects.exists())


class ValidateEventPageViewErrorTest(TestCase):

    def setUp(self):
        self.page_view = {
            "session_id": "d66ac88b-f801-4984-953f-5c6b266494a0",
            "category": "page interaction",
            "name": "pageview",
            "data": {},
            "timestamp": "2022-04-01 00:00:0.000000"
        }

    def test_invalid_payload_page_view(self):
        with self.assertRaises(SerializerError):
            validate_event(self.page_view)


class ValidateEventPageClickSuccessTest(TestCase):

    def setUp(self):
        page_click = {
            "session_id": "d66ac88b-f801-4984-953f-5c6b266494a0",
            "category": "page interaction",
            "name": "link click",
            "data": {
                "host": "www.cwtech.dev",
                "path": "/",
                "element": "register"
            },
            "timestamp": "2022-04-01 00:00:0.000000"
        }
        validate_event(page_click)

    def test_create_event(self):
        self.assertTrue(Event.objects.exists())

    def test_create_page_click(self):
        self.assertTrue(PageClick.objects.exists())


class ValidateEventPageClickErrorTest(TestCase):

    def setUp(self):
        self.page_click = {
            "session_id": "d66ac88b-f801-4984-953f-5c6b266494a0",
            "category": "page interaction",
            "name": "link click",
            "data": {
                "host": "www.cwtech.dev",
                "path": "/",
                "element": "register",
                "foo": "bar"
            },
            "timestamp": "2022-04-01 00:00:0.000000"
        }

    def test_invalid_payload_page_click(self):
        with self.assertRaises(SerializerError):
            validate_event(self.page_click)
            self.assertRaisesMessage(SerializerError, 'Payload Invalid!')


class ValidateEventEventFormSuccessTest(TestCase):

    def setUp(self):
        event_form = {
            "session_id": "d66ac88b-f801-4984-953f-5c6b266494a0",
            "category": "form interaction",
            "name": "submit",
            "data": {
                "host": "www.cwtech.dev",
                "path": "/",
                "form": {
                    "first_name": "Jose",
                    "last_name": "Barroso"
                }
            },
            "timestamp": "2022-04-01 00:00:0.000000"
        }
        validate_event(event_form)

    def test_create_event(self):
        self.assertTrue(Event.objects.exists())

    def test_create_event_form(self):
        self.assertTrue(EventForm.objects.exists())

    def test_create_account(self):
        self.assertTrue(EventForm.objects.exists())


class ValidateEventEventFormErrorTest(TestCase):

    def setUp(self):
        self.event_data = {
            "session_id": "d66ac88b-f801-4984-953f-5c6b266494a0",
            "category": "form interaction",
            "name": "submit",
            "data": {
                "host": "www.cwtech.dev",
                "path": "/",
                "element": "register",
                "foo": "bar"
            },
            "timestamp": "2022-04-01 00:00:0.000000"
        }

    def test_invalid_payload_page_click(self):
        with self.assertRaises(SerializerError):
            validate_event(self.event_data)
            self.assertRaisesMessage(SerializerError, 'Payload Invalid!')


class ValidateEventEventDataErrorTest(TestCase):

    def setUp(self):
        self.event_data = {
            "session_id": "d66ac88b-f801-4984-953f-5c6b266494a0",
            "name": "foo",
            "category": "bar",
            "data": {"foo": "bar"},
            "timestamp": "2022-04-01 00:00:0.000000"
        }

    def test_invalid_event_data(self):
        with self.assertRaises(InvalidPayload):
            validate_event(self.event_data)
            self.assertRaisesMessage(InvalidPayload, 'Payload not found!')


class ValidateEventPayloadNotFoundTest(TestCase):

    def setUp(self):
        self.event_form = {
            "session_id": "d66ac88b-f801-4984-953f-5c6b266494a0",
            "name": "submit",
            "data": {"foo": "bar"},
            "timestamp": "2022-04-01 00:00:0.000000"
        }

    def test_invalid_event_data(self):
        with self.assertRaises(SerializerError):
            validate_event(self.event_form)
            self.assertRaisesMessage(SerializerError, 'Event Invalid!')
