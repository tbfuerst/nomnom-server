from django.test import TestCase

# Create your tests here.

from .models import Account_Type_Templates

# Run all tests with python3 manage.py test nomnom


class Account_Type_Templates_Model_Tests(TestCase):
    def testfunction(self):
        modelData = Account_Type_Templates(account_type_id=101,
                                           account_type_name="various",
                                           account_type_description="various")

        isInteger = isinstance(modelData.account_type_id, int),

        self.assertIs(isInteger, True)  # output and expected output
