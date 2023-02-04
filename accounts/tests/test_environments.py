from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Environment

class EnvironmentsTestCase(TransactionTestCase):
	fixtures = ['users.json']


	def setUp(self):
		pass

	def testEnvironmentCrud(self):
		with self.settings(ALLOWED_HOSTS=('example.com',)):
			self.client.force_login(get_user_model().objects.first())
			
			response = self.client.get(
				reverse('accounts:environment_list'),
				HTTP_HOST='example.com'
			)
			self.assertNotContains(response, 'data-bs-target="#delete')
			self.assertTemplateUsed(response, 'accounts/environment_list.html')

			self.assertRedirects(
				self.client.post(
					reverse('accounts:environment_create'), 
					{'name': 'test_environment'},
					HTTP_HOST='example.com'
				),
				reverse('accounts:environment_list')
			)

			self.assertContains(
				self.client.get(
					reverse('accounts:environment_list'),
					HTTP_HOST='example.com'
				), 
				'data-bs-target="#delete',
				count=1
			)			

			environment = Environment.objects.first()
			self.assertEquals('test_environment', environment.name)
			
			self.assertRedirects(
				self.client.post(
					reverse('accounts:environment_create'), 
					{
						'name': 'test_environment2',
						'source_environment' : environment.pk
					},
					HTTP_HOST='example.com'
				),
				reverse('accounts:environment_list')
			)