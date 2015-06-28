# coding=utf-8
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site
from quizme.core.utils import send_email
from .models import Receipt


@receiver(post_save, sender=Receipt)
def email_receipt(sender, **kwargs):
	if kwargs['created']:
		r = kwargs['instance']

		send_email(
			subject = 'Kvitto på ditt köp från QuizMe.se',
			template_name = 'receipt',
			email = r.account.email,
			context = {
				'receipt': r, 
				'site_url': Site.objects.get_current().domain
			}
		)
