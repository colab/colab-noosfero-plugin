
from colab.plugins.utils.apps import ColabPluginAppConfig
from colab.signals.signals import register_signal


class NoosferoPluginAppConfig(ColabPluginAppConfig):
    name = 'colab_noosfero'
    verbose_name = 'Noosfero Plugin'
    namespace = 'noosfero'

    registered_signals = ['community_creation']
    short_name = 'noosfero'

    def register_signal(self):
        register_signal(self.short_name, self.registered_signals)
