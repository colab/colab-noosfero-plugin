from django.db.models.signals import pre_save
from django.dispatch import receiver
from colab_noosfero.models import NoosferoCommunity
from django.core.exceptions import ObjectDoesNotExist
from colab.signals.signals import send


@receiver(pre_save, sender=NoosferoCommunity)
def verify_community_creation(sender, **kwargs):
    community = kwargs.get('instance')
    try:
        NoosferoCommunity.objects.get(pk=community.id)
    except ObjectDoesNotExist:
        send('community_creation', 'noosfero', community=sender)
    else:
        send('community_updated', 'noosfero', community=sender)
