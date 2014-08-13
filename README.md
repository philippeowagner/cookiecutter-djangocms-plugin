cookiecutter-djangocms-plugin
=============================

[Cookiecutter](https://github.com/audreyr/cookiecutter) template to get started with
[custom plugins](http://django-cms.readthedocs.org/en/latest/extending_cms/custom_plugins.html) for [django-cms](https://github.com/divio/django-cms).


Installation and Usage
------------

Install cookiecutter:

    $ pip install cookiecutter

Change directory to where you want to install the plugin. For example:

    $ cd apps/website/plugins/

Now run the cookiecutter command against this repo

    $ cookiecutter https://github.com/mishbahr/cookiecutter-djangocms-plugin.git

You'll be prompted to enter values. Then it'll create a plugin in the current 
working directory, based on those values. For example:

    Cloning into 'cookiecutter-djangocms-plugin'...
    remote: Counting objects: 23, done.
    remote: Compressing objects: 100% (18/18), done.
    remote: Total 23 (delta 4), reused 15 (delta 1)
    Unpacking objects: 100% (23/23), done.
    Checking connectivity... done.
    package_name (default is "myplugin")? link
    plugin_name (default is "MyCMSPlugin")? LinkPlugin
    model_name (default is "MyCMSPluginModel")? Link
    plugin_verbose_name (default is "My CMS Plugin")? Link
    plugin_module (default is "Generic")?
    version (default is "0.0.1")?
    description (default is "A short description of this plugin.")? A link plugin for django CMS
    text_enabled (default is "n")? y
    allow_children (default is "n")? y

Now take a look at your new plugin. Also don’t forget to add the newly created plugin to `settings.INSTALLED_APPS`.

    link/
      ├── __init__.py
      ├── cms_plugins.py
      ├── models.py
      └── templates
        └── cms
          └── plugins
            └── link.html
            
    3 directories, 4 files
    

**cms_plugins.py**

    # -*- coding: utf-8 -*-
    from django.utils.translation import ugettext_lazy as _

    from cms.plugin_base import CMSPluginBase
    from cms.plugin_pool import plugin_pool

    from .models import Link


    class LinkPlugin(CMSPluginBase):
        """A link plugin for django CMS"""

        module = _('Generic')
        name = _('Link')
        model = Link
        render_template = 'cms/plugins/link.html'

        text_enabled = True
        
    	allow_children = True
    	
        def render(self, context, instance, placeholder):
            context = super(LinkPlugin, self) \
                .render(context, instance, placeholder)
            return context

        plugin_pool.register_plugin(LinkPlugin)

**models.py**

    # -*- coding: utf-8 -*-
    from django.db import models
    from django.utils.translation import ugettext_lazy as _

    from cms.models import CMSPlugin


    class Link(CMSPlugin):
        """A link plugin for django CMS"""

        pass
        
**link.html** (plugin template) 

    {% load cms_tags %}

    <div class="link">
        {% for plugin in instance.child_plugin_instances %}
        	{% render_plugin plugin %}
        {% endfor %}
    </div>
    

Awesome, right? 
  
Useful Links
------------

- [cookiecutter documentation](http://cookiecutter-django-cms.readthedocs.org/)
- [django-cms plugins documentation](http://django-cms.readthedocs.org/en/latest/extending_cms/custom_plugins.html)
