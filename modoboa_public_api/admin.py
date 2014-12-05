from django.contrib import admin

from .models import ModoboaInstance


class ModoboaInstanceAdmin(admin.ModelAdmin):

    """
    Admin class for ModoboaInstance model.
    """

    list_display = ("ip_address", "hostname", "known_version")


admin.site.register(ModoboaInstance, ModoboaInstanceAdmin)