from django.db import models
from django.utils import simplejson
from django.core.urlresolvers import reverse


class ModelMixIn(object):
    FIELD_NAMES = []
    FIELD_LABELS = {}

    @classmethod
    def field_labels(cls):
        """
            get fields verbose_name use fields_names
        """
        if cls.FIELD_LABELS:
            return cls.FIELD_LABELS

        def get_label(fname):
            return cls._meta.get_field_by_name(fname)[0].verbose_name

        field_names = cls.fields_names()
        for field_name in field_names:
            cls.FIELD_LABELS[field_name] = get_label(field_name)
        return cls.FIELD_LABELS

    @classmethod
    def fields_names(cls):
        """
            get fields names
        """
        if cls.FIELD_NAMES:
            return cls.FIELD_NAMES
        cls.FIELD_NAMES = [field.name for field in cls._meta.fields]
        cls.FIELD_NAMES.sort()
        return cls.FIELD_NAMES


class Person(ModelMixIn, models.Model):
    first_name = models.CharField('Name', max_length=35)
    last_name = models.CharField('Last name', max_length=35)
    birthday = models.DateField('Date of birth')
    bio = models.TextField('Bio')
    email = models.EmailField('E-mail')
    jabber = models.CharField('Jabber', max_length=35)
    skype = models.CharField('Skype', max_length=35)
    other_contacts = models.TextField('Other contacts')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('person_detail')


class RequestStore(ModelMixIn, models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.TextField()
    req_get = models.TextField(blank=True, null=True)
    req_post = models.TextField(blank=True, null=True)
    req_cookies = models.TextField(blank=True, null=True)
    req_session = models.TextField(blank=True, null=True)
    req_meta = models.TextField()
    res_status_code = models.PositiveIntegerField()

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.req_get = dict(self.req_get)
        self.req_post = dict(self.req_post)
        self.req_session = dict(self.req_session.items())
        return super(RequestStore, self).save(*args, **kwargs)

    def __unicode__(self):
        return "(%s) '%s' at %s" % (self.res_status_code,
                                    self.url,
                                    self.created)
