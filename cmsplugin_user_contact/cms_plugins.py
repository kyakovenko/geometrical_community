# -*- coding: utf-8 -*-
__author__ = 'Kirill S. Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cmsplugin_contact.cms_plugins import ContactPlugin

from models import UserContact
from forms import UserContactForm, UserContactAdminForm


class UserContactPlugin(ContactPlugin):
    name = _("User Contact Form")

    model = UserContact
    form = UserContactAdminForm
    contact_form = UserContactForm

    # We're using the original cmsplugin_contact templates here which
    # works fine but requires that the original plugin is in INSTALLED_APPS.
    email_template = "cmsplugin_user_contact/email.txt"
    render_template = "cmsplugin_user_contact/contact.html"
    subject_template = "cmsplugin_user_contact/subject.txt"
    change_form_template = "admin/cms/page/plugin_change_form.html"

    fieldsets = (
        (None, {'fields': ('site_email', 'email_label', 'sender_label', 'thanks', 'submit'), }),
        #(_('Spam Protection'), {'fields': ('spam_protection_method', 'akismet_api_key',
        #                                   'recaptcha_public_key', 'recaptcha_private_key',
        #                                   'recaptcha_theme')
        #})
    )

plugin_pool.unregister_plugin(ContactPlugin)
plugin_pool.register_plugin(UserContactPlugin)