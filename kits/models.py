from django.db import models

# Kit Model
class Kit(models.Model):
    kit_id = models.IntegerField(db_column='KitID', primary_key=True)  # Use KitID as the primary key
    kit_name = models.CharField(db_column='KitName', max_length=255)  # KitName column
    pump_model = models.CharField(db_column='PumpModel', max_length=255)  # PumpModel column

    class Meta:
        managed = False  # We are not managing the database table creation
        db_table = 'Kits'  # Name of the existing table


# Level1Component Model
class Level1Component(models.Model):
    part_id = models.IntegerField(db_column='PartID', primary_key=True)  # PartID as the primary key
    item_number = models.CharField(db_column='ItemNumber', max_length=255)
    parent_kit = models.ForeignKey(Kit, db_column='ParentKit', on_delete=models.CASCADE)  # ForeignKey to Kit
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)
    drawing_number = models.CharField(db_column='DrawingNumber', max_length=255, blank=True, null=True)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)
    parent_item = models.CharField(db_column='ParentItem', max_length=255, blank=True, null=True)

    class Meta:
        managed = False  # We are not managing the database table creation
        db_table = 'Level1Components'  # Name of the existing table


# Level2Component Model
class Level2Component(models.Model):
    part_id = models.IntegerField(db_column='PartID', primary_key=True)  # PartID as the primary key
    item_number = models.CharField(db_column='ItemNumber', max_length=255)
    parent_part = models.ForeignKey(Level1Component, db_column='ParentPartID', on_delete=models.CASCADE)  # ForeignKey to Level1Component
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)
    drawing_number = models.CharField(db_column='DrawingNumber', max_length=255, blank=True, null=True)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)

    class Meta:
        managed = False  # We are not managing the database table creation
        db_table = 'Level2Components'  # Name of the existing table


# KitParts Model
class KitPart(models.Model):
    kit_part_id = models.AutoField(db_column='KitPartID', primary_key=True)  # Auto-incrementing primary key
    kit = models.ForeignKey(Kit, db_column='KitID', on_delete=models.CASCADE)  # ForeignKey to Kit
    part = models.ForeignKey(Level1Component, db_column='PartID', on_delete=models.CASCADE)  # ForeignKey to Level1Component
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)

    class Meta:
        managed = False  # We are not managing the database table creation
        db_table = 'KitParts'  # Name of the existing table
