from django.utils import timezone

from rest_framework import serializers

from .models import Event, PageView, PageClick, Account, EventForm


class ValidatePayload:
    def has_unknowns(self, attrs):
        """Verify if the data informed has unknown fields"""
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            errors = ", ".join(unknown)
            raise serializers.ValidationError(f"Unknown field(s): {errors}")
        return attrs


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


class PageViewSerializer(serializers.ModelSerializer, ValidatePayload):
    class Meta:
        model = PageView
        exclude = ('event', )

    def validate(self, attrs):
        attrs = super().has_unknowns(attrs)
        return super().validate(attrs)


class PageClickSerializer(serializers.ModelSerializer, ValidatePayload):
    class Meta:
        model = PageClick
        exclude = ('event', )

    def validate(self, attrs):
        attrs = super().has_unknowns(attrs)
        return super().validate(attrs)


class AccountSerializer(serializers.ModelSerializer, ValidatePayload):
    class Meta:
        model = Account
        exclude = ('event_form', )

    def validate(self, attrs):
        attrs = super().has_unknowns(attrs)
        return super().validate(attrs)


class EventFormSerializer(serializers.ModelSerializer, ValidatePayload):
    form = serializers.DictField()

    class Meta:
        model = EventForm
        exclude = ('event', )

    def validate(self, attrs):
        attrs = super().has_unknowns(attrs)

        # This will verify if the form content has the expected fields
        form_data = self.initial_data.get("form", {})
        account_serializer = AccountSerializer(data=form_data)
        # If the validation doesn't work, an exception will raise.
        account_serializer.is_valid(raise_exception=True)

        return super().validate(attrs)

    def create(self, validated_data):
        account_data = validated_data.pop('form', None)

        # Creates the event_form record and returns the ID required for
        # the account record.
        event_form = EventForm.objects.create(**validated_data)
        event_form.save()

        account_data["event_form_id"] = event_form.id

        account = Account.objects.create(**account_data)
        account.save()

        return event_form
