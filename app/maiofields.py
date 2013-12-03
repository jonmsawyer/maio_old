import uuid

#import maio.settings
from django.db import models

class FixedCharField(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(FixedCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % (self.max_length,)

class UUIDField(FixedCharField):
    __metaclass__ = models.SubfieldBase
    description = "Universally Unique Identifier (See RFC 4122)"
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 36
        super(UUIDField, self).__init__(*args, **kwargs)
    
    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
            return 'uuid'
        
        return 'char(%s)' % (self.max_length,)
    
    def pre_save(self, instance, add):
        try:
            value = getattr(instance, self.attname, None)
        except:
            value = None
        if not value:
            value = str(uuid.uuid4())
            try:
                setattr(instance, self.attname, value)
            except:
                pass
        return value

    def to_python(self, value):
        if not value:
            return
        return value

    def get_db_prep_save(self, value, connection):
        if not value:
            return
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        if not value:
            return
        return value

