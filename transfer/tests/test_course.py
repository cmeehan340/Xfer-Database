from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from ..models.models_transfer import Course


class MajorRequirmentTest(TestCase):
        def setUp(self):
            self.user = get_user_model().objects.create_user(
                username='testuser',
                email='test@email.com',
                password='secret'
            )
            self.course = Course.objects.create(
                subject_no = 'COMP 705',
                title = "Full Stack Development",
                sem_year_taken = 'Spring 2020',
                expiration_date = '2022-04-08',
                approved_status = 'Y',
                comment = 'This is a test comment',
                approver_id = 
            )

        def test_string_representation(self):
            name = Course(title='Object Oriented Software')
            self.assertEqual(str(name), name.title)
