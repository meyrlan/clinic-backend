from django.utils.translation import gettext_lazy as _

from django.apps import AppConfig

from common.app_config import BaseAppConfig


class CoreConfig(BaseAppConfig):
    name = "core"
    label = "core"
    verbose_name = _("Core")
