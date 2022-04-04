from django.test import TestCase

from the_eye.serializers import PageViewSerializer, EventFormSerializer


class ValidatePayloadSuccessTest(TestCase):

    def setUp(self):
        page_view_paylod = {
            "host": "www.cwtech.dev",
            "path": "/",
            "invalid_field": "invalid value"
        }
        self.payload_serializer = PageViewSerializer(data=page_view_paylod)
        self.payload_serializer.is_valid()

    def test_has_errors(self):
        self.assertTrue(self.payload_serializer.errors)

    def test_has_unknown_error(self):
        self.assertIn("non_field_errors", self.payload_serializer.errors)

    def test_unknown_message(self):
        _assert = self.payload_serializer.errors['non_field_errors'][0]
        expected = "Unknown field(s): invalid_field"
        self.assertEqual(expected, _assert)


class ValidatePayloadEventFormSerializerSuccessTest(TestCase):

    def setUp(self):
        page_view_paylod = {
            "host": "www.cwtech.dev",
            "path": "/",
            "form": {
                "first_name": "John",
                "last_name": "Doe",
                "password": "invalid value",
                "other_name": "invalid value"
            }
        }
        self.payload_serializer = EventFormSerializer(data=page_view_paylod)
        self.payload_serializer.is_valid()

    def test_has_errors(self):
        self.assertTrue(self.payload_serializer.errors)

    def test_has_unknown_error(self):
        self.assertIn("non_field_errors", self.payload_serializer.errors)

    def test_unknown_message(self):
        _assert = self.payload_serializer.errors['non_field_errors'][0]
        expected = "Unknown field(s): other_name, password"
        self.assertEqual(expected, _assert)
