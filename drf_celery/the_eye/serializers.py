from django.utils import timezone

from rest_framework import serializers

from .models import Event, PageView, PageClick, Account, EventForm


class EventSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    data = serializers.DictField()

    class Meta:
        model = Event
        fields = '__all__'

    def validate_timestamp(self, value):
        """
        Check if the timestamp is in the future
        """
        if value > timezone.now():
            raise serializers.ValidationError("The timestamp is in the future!")
        return value


class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageView
        exclude = ('event', )


class PageClickSerializer(serializers.Serializer):
    class Meta:
        model = PageClick
        exclude = ('event', )


class AccountSerializer(serializers.Serializer):
    class Meta:
        model = Account
        exclude = ('event_form', )


class EventFormSerializer(serializers.Serializer):
    form = AccountSerializer()

    class Meta:
        model = EventForm
        exclude = ('event', )

    def create(self, validated_data):
        account_data = validated_data.pop('form', None)

        event_form = EventForm.objects.create(**validated_data)
        event_form.save()

        account_data["event_form_id"] = event_form.id

        account = Account.objects.create(**account_data)
        account.save()

        return event_form
