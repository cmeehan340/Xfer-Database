'''
test_course.py
Chris Meehan
4/12/2020
'''
from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models.model_course import Course


class CourseTest(TestCase):
    '''
    This class is deigned to test the Major Requirement Model.
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
        self.course = Course.objects.create(
            subject_no='COMP 705',
            title="Full Stack Development",
            sem_year_taken='Sp2020',
            expiration_date='2022-04-08',
            approved_status='Y',
            comment='This is a test comment',
            # approver_id =
        )

    def test_string_representation(self):
        '''
        Runs a test to verify name is added and represented correctly
        '''
        name = Course(title='Object Oriented Software')
        self.assertEqual(str(name), name.title)

    def test_course_content(self):
        '''
        Runs a test to verify that the course is being created correctly
        '''
        self.assertEqual(f'{self.course.subject_no}', 'COMP705')
        self.assertEqual(f'{self.course.title}', 'Full Stack Development')
        self.assertEqual(f'{self.course.sem_year_taken}', 'Sp2020')
        self.assertEqual(f'{self.course.expiration_date}', '2022-04-08')
        self.assertEqual(f'{self.course.approved_status}', 'Y')
        self.assertEqual(f'{self.course.comment}', 'This is a test comment')
