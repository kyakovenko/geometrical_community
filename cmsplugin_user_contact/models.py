# -*- coding: utf-8 -*-
__author__ = 'Kirill S. Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

from django.db import models
from cmsplugin_contact.models import BaseContact
from django.utils.translation import ugettext_lazy as _


class UserContact(BaseContact):
    sender_label = models.CharField(_('Name'), max_length=128)
