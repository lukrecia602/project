from django.contrib import admin
from . models import mnb_deviza, mnb_name_good, mnb_name, Tranzakciok

admin.site.register(mnb_deviza)
admin.site.register(mnb_name_good)
admin.site.register(mnb_name)
admin.site.register(Tranzakciok)