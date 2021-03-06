# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InitUserTag(models.Model):
    user_id = models.IntegerField()
    anime = models.IntegerField()
    movie = models.IntegerField()
    game = models.IntegerField()
    beautiful_woman = models.IntegerField()
    car = models.IntegerField()
    excercise = models.IntegerField()
    food = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'init_user_tag'


class Uplisttovideo(models.Model):
    upid = models.CharField(max_length=45)
    videoid = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'uplisttovideo'


class Video(models.Model):
    video_id = models.CharField(max_length=45)
    video_name = models.CharField(max_length=100)
    up_id = models.CharField(max_length=45)
    video_url = models.CharField(max_length=1000, blank=True, null=True)
    cover_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video'


class VideoTag(models.Model):
    id = models.IntegerField(primary_key=True)
    video_id = models.IntegerField()
    anime = models.IntegerField()
    movie = models.IntegerField()
    game = models.IntegerField()
    beautiful_woman = models.IntegerField()
    car = models.IntegerField()
    excercise = models.IntegerField()
    food = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'video_tag'
