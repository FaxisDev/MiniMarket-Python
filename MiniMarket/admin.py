from django.contrib.admin import AdminSite
#from django.utils.translation import ugettext_lazy

class MiniMarketAdmin(AdminSite):
    site_header = 'Panel de administracion'
    site_title = 'MiniMarket - Proyecto Michel Valencia'
    index_title = 'Bienvenido al panel de administrador MiniMarket 1.0'

# Registra tu clase personalizada de AdminSite
admin_site = MiniMarketAdmin(name='miadmin')
