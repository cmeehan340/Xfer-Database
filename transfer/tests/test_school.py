from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from ..models.models_transfer import School

# Create your tests here.

class SchoolTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.school = School.objects.create(
            school_name = 'test School Name',
        )

    def test_string_representation(self):
        school = School(school_name='a school')
        self.assertEqual(str(school), school.school_name)
