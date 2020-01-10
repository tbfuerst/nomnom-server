from django.db import models

# Create your models here.


class Tag_Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def ___str___(self):
        return self.name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Tag_Category, on_delete=models.CASCADE)

    def ___str___(self):
        return self.name





# class Account_Template(models.Model):
#     id = models.AutoField(primary_key=True)
#     template_identifier = models.CharField(max_length=64)
#     type_template = models.OneToOneField(
#         Account_Type_Template, on_delete=models.CASCADE, default=None)
#     account_numbers = models.CharField(max_length=2000*10)
#     account_names = models.CharField(max_length=2000*128)
#     account_descriptions = models.CharField(max_length=2000*255)
#     type_ids = models.CharField(max_length=2000*5)


# def __str__(self):
#     return self.template_identifier


# class Account_Type(models.Model):
#     id = models.AutoField(primary_key=True)
#     type_id = models.PositiveIntegerField()
#     name = models.CharField(max_length=64)
#     description = models.CharField(max_length=255)

#     def __int__(self):
#         return self.type_id

#     # Inner class for Metainformation such as order_by like shown here
#     class Meta:
#         ordering = ['type_id']


# class Account(models.Model):
#     id = models.AutoField(primary_key=True)
#     number = models.CharField(max_length=8)
#     name = models.CharField(max_length=64)
#     description = models.CharField(max_length=255)
#     type_id = models.ForeignKey(Account_Type, on_delete=models.CASCADE)
#     is_deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name


# class Area(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=64)
#     description = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


# class Transaction_Tag(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=32)

#     def __str__(self):
#         return self.name


# class Transaction(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     book_date = models.DateTimeField(auto_now=True)
#     stack_id = models.BigIntegerField(default=0)
#     area = models.ForeignKey(Area, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Transaction_Tag)

#     # if FK of Accounts is removed, Remove all Transactions related to Accounts
#     account_id = models.ForeignKey(
#         Account, on_delete=models.CASCADE, related_name='account')
#     c_account_id = models.ForeignKey(
#         Account, on_delete=models.CASCADE, related_name='C_account')
#     description = models.CharField(max_length=255)
#     amount = models.DecimalField(
#         decimal_places=2, max_digits=24, default=0.00)

#     def __int__(self):
#         return self.stack_id

#     def customFunction(self):
#         return self.amount * 2


# class Settings(models.Model):
#     id = models.AutoField(primary_key=True)
#     std_bank_acc = models.OneToOneField(
#         Account, on_delete=models.CASCADE, related_name='std_bank')
#     std_cash_acc = models.OneToOneField(
#         Account, on_delete=models.CASCADE, related_name='std_cash')
#     primary_swatch = models.CharField(max_length=16)
#     sec_color = models.CharField(max_length=16)
#     tert_color = models.CharField(max_length=16)

#     def __int__(self):
#         return self.id
