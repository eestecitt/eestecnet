from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.events.models import BaseEvent, Exchange, Training, Workshop, Travel


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class BaseEventSerializer(ModelSerializer):
    class Meta:
        model = BaseEvent

    owner = HiddenField(
        default=CurrentUserDefault()
    )

class ExchangeSerializer(BaseEventSerializer):
    class Meta:
        model = Exchange


class TrainingSerializer(BaseEventSerializer):
    class Meta:
        model = Training


class WorkshopSerializer(BaseEventSerializer):
    class Meta:
        model = Workshop


class TravelSerializer(ModelSerializer):
    class Meta:
        model = Travel