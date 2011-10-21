"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from models import Person
from django.test import TestCase
from django.core.urlresolvers import reverse


class TestModelBase:

    def setUp(self):
        self.objects_count = self.model.objects.count()
        self.field_list.sort()

    def test_fixture(self):
        self.assertEqual(self.objects_count, self.fixture_count)

    def test_fields(self):
        self.assertEqual(self.field_list, self.model.fields_names())


class TestModelPerson(TestModelBase, TestCase):
    model = Person
    fixture_count = 1
    field_list = ['id', 'first_name', 'last_name', 'birthday', 'bio', 'email',
                  'jabber', 'skype', 'other_contacts']


class TestPersonView(TestCase):
    url = reverse('person_detail')


    def setUp(self):
        self.person = Person.objects.get(pk=1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)

    def test_context(self):
        context_person = self.response.context['person']
        self.assertEqual(str(context_person), str(self.person))

    def test_layout(self):
        self.assertContains(self.response, self.person.bio)
        self.assertContains(self.response, self.person.first_name)
        self.assertContains(self.response, self.person.jabber)
        self.assertContains(self.response, self.person.skype)



