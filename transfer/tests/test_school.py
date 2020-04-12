'''
test_school.py
Chris Meehan
4/12/2020
'''
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from ..models.model_school import School

# Create your tests here.

class SchoolTests(TestCase):
    '''
    This class is designed to test the schools model
    '''
    def setUp(self):
        '''
        Sets up the test
        '''
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.school = School.objects.create(
            school_name='test School Name',
        )

    def test_string_representation(self):
        '''
        Runs a test to verify description is added and represented correctly
        '''
        school = School(school_name='a school')
        self.assertEqual(str(school), school.school_name)
