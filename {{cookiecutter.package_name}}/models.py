# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class {{cookiecutter.model_name}}(CMSPlugin):
    """{{cookiecutter.description}}"""

    pass

