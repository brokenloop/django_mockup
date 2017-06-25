# from django.db import models
#
#
# class Stop(models.Model):
#     lat = models.FloatField()
#     lon = models.FloatField()
#     name = models.CharField(max_length=250)
#     stop_id = models.IntegerField()
#
#
# class Route(models.Model):
#     stop = models.Foreignkey(Stop, on_delete=models.CASCADE)
#     route_id = models.IntegerField()
#     order = models.IntegerField()