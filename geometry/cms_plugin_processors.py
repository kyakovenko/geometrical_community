# -*- coding: utf-8 -*-
__author__ = 'Kirill S. Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

from django.template.loader import render_to_string


def wrap_content(instance, placeholder, rendered_content, original_context):
    if placeholder.page:
        if original_context.get('plugin_index') % 2 == 0:
            return render_to_string('cms/white-wrapper.html', {"content": rendered_content})
        else:
            return render_to_string('cms/gray-wrapper.html', {"content": rendered_content})
    else:
        return rendered_content