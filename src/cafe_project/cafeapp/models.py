from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Order(models.Model):
    table_no = models.IntegerField()
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Table {self.table_no} - {self.item.name}"
