from rest_framework import serializers


class EventSerializer(serializers.Serializer):
    session_id = serializers.UUIDField()
    category = serializers.CharField()
    name = serializers.CharField()
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    data = serializers.DictField()

    # def validate_timestamp(self, attrs, source):
    #     """
    #     Check if the timestamp is in the future
    #     """
    #     value = attrs[source]
    #     if value > datetime.now():
    #         raise serializers.ValidationError("The timestamp is in the future!")
    #     return attrs


class PageViewSerializer(serializers.Serializer):
    host = serializers.CharField()
    path = serializers.CharField()


class PageClickSerializer(serializers.Serializer):
    host = serializers.CharField()
    path = serializers.CharField()
    element = serializers.CharField()


class AccountFieldsSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class AccountSubmitFormSerializer(serializers.Serializer):
    host = serializers.CharField()
    path = serializers.CharField()
    form = AccountFieldsSerializer()
