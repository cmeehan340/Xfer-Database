'''
test_major_req.py
Chris Meehan
4/12/2020
'''
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from ..models.model_requirement import MajorRequirment


class MajorRequirmentTest(TestCase):
    '''
    This class is designed to test the major requirements model
    '''
    def set_up(self):
        '''
        Sets up the test
        '''
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.major_req = MajorRequirment.objects.create(
            description='test description',
        )

    def test_string_representation(self):
        '''
        Runs a test to verify description is added and represented correctly
        '''
        req = MajorRequirment(description='this is a test')
        self.assertEqual(str(req), req.description)
