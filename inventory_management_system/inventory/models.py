from django.db import models

# Create your models here.

class Donation(models.Model):

    description = models.CharField(max_length=200, blank=False, default='Describe the Item Here')


    choices = ( #for status
        ('AVAILABLE', 'Item ready to be picked up'),
        ('RESERVED', 'Item reserved by another user'),
        ('RESTOCKING', 'Item may be stocked soon')
    )


    expiry = models.CharField(max_length=200, blank=False, default='Enter expiration date')
    status = models.CharField(max_length=10, choices=choices, default='AVAILABLE')
    misc = models.CharField(max_length=50, default="Any misc info about your item")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0}'.format(self.type)

class Foods(Donation):
    pass

class Drinks(Donation):
    pass

class MiscObjects(Donation):
    pass


# class Foods(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
#
#
# class Drinks(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
#
#
# class MiscObjects(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
