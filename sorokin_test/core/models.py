from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


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


class RequestStore(ModelMixIn, models.Model):
    PRIORITY_CHOICES = [[1, 1],
                        [2, 2],
                        [3, 3],
                        [4, 4],
                        [5, 5]]
    created = models.DateTimeField(auto_now_add=True)
    url = models.TextField()
    req_get = models.TextField(blank=True, null=True)
    req_post = models.TextField(blank=True, null=True)
    req_cookies = models.TextField(blank=True, null=True)
    req_session = models.TextField(blank=True, null=True)
    req_meta = models.TextField()
    req_status_code = models.PositiveIntegerField(blank=True, null=True)
    priority = models.IntegerField(default=1, choices=PRIORITY_CHOICES)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return "(%s) '%s' at %s" % (self.req_status_code,
                                    self.url,
                                    self.created)


class DbEntry(ModelMixIn, models.Model):
    ACTION_CHOICES = (
                ('create', 'Create'),
                ('edit', 'Edit'),
                ('delete', 'Delete'),
            )
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    presentation = models.CharField(max_length=255)
    action = models.CharField(max_length=35, choices=ACTION_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s %s: %s' % (self.created, self.action, self.presentation)
