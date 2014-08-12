# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import {{cookiecutter.model_name}}


class {{ cookiecutter.plugin_name}}(CMSPluginBase):
    """{{cookiecutter.description}}"""

    module = _('{{ cookiecutter.plugin_module }}')
    name = _('{{ cookiecutter.plugin_verbose_name }}')
    model = {{ cookiecutter.model_name }}
    render_template = 'cms/plugins/{{ cookiecutter.package_name }}.html'
{% if cookiecutter.text_enabled == "y" or cookiecutter.text_enabled == "Y" %}
    text_enabled = True
{% elif cookiecutter.allow_children == "y" or cookiecutter.allow_children == "Y" %}
    allow_children = True
{% endif%}
    def render(self, context, instance, placeholder):
        context = super({{ cookiecutter.plugin_name}}, self) \
            .render(context, instance, placeholder)
        return context

plugin_pool.register_plugin({{ cookiecutter.plugin_name}})
