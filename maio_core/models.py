import uuid

from django.db import models
from django.db.models import Q

from .maiofields import FixedCharField


mimetype_extension = {
    'image': {
        'image/gif': '.gif',
        'image/jpeg': '.jpg',
        'image/pjpeg': '.jpg',
        'image/png': '.png',
        'image/svg+xml': '.svg',
        'image/tiff': '.tiff',
        'image/bmp': '.bmp',
        'image/x-windows-bmp': '.bmp',
        'image/x-tiff': '.tiff',
    }
}

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)
    count = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    left_node = models.PositiveIntegerField(null=True, blank=True) # for v2
    right_node = models.PositiveIntegerField(null=True, blank=True) # for v2

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    mime_type = models.CharField(max_length=255)
    size = models.PositiveIntegerField(default=0)
    mtime = models.FloatField()
    md5sum = FixedCharField(max_length=32)
    tn_path = models.CharField(max_length=1024)
    file_path = models.CharField(max_length=1024)
    file_path_hash = FixedCharField(max_length=32, unique=True)
    rating = models.SmallIntegerField(null=True)
    views = models.PositiveIntegerField(default=0)
    media_length = models.PositiveIntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['file_path']

    @staticmethod
    def get_all_images():
        Qr = None
        for key, value in mimetype_extension['image'].items():
            q = Q(**{"mime_type__exact": key})
            if Qr:
                Qr = Qr | q
            else:
                Qr = q
            
        files = File.objects.all().filter(Qr)
        return files

    def file_name(self):
        return self.file_path.split('/')[-1]
    
class FileCaption(models.Model):
    file = models.OneToOneField(File, primary_key=True) 
    caption = models.TextField()

class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True)
    views = models.PositiveIntegerField(default=0)
    default_order = models.PositiveSmallIntegerField(default=0) # 0 random, 1 descending, 2 ascending
    time_between = models.PositiveIntegerField(default=5) # seconds
    media_class = models.PositiveSmallIntegerField(default=0) # 0 other, 1 image, 2 video, 3 audio, 4 text

class AssocPlaylistFile(models.Model):
    playlist = models.ForeignKey(Playlist)
    file = models.ForeignKey(File)
    sort = models.PositiveIntegerField()
