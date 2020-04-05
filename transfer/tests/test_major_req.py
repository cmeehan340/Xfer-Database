from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from ..models.models_transfer import MajorRequirment


class MajorRequirmentTest(TestCase):
        def setUp(self):
            self.user = get_user_model().objects.create_user(
                username='testuser',
                email='test@email.com',
                password='secret'
            )
            self.major_req = MajorRequirment.objects.create(
                description = 'test description',
            )

        def test_string_representation(self):
            req = MajorRequirment(description='this is a test')
            self.assertEqual(str(req), req.description)
