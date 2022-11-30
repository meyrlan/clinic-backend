import logging

from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_extra_fields.fields import Base64ImageField
from django.db import transaction


logger = logging.getLogger(__name__)


