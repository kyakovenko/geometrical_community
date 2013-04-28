# -*- coding: utf-8 -*-
__author__ = 'Kirill S. Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

from django.template.loader import render_to_string


def wrap_content(instance, placeholder, rendered_content, original_context):
    if placeholder.slot != 'content' or instance.plugin_type == 'TextPlugin' \
            or (instance._render_meta.text_enabled and instance.parent):
        return rendered_content
    else:
        return render_to_string('cms/gray-wrapper.html', {"content": rendered_content})