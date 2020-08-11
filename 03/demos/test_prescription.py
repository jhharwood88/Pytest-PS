import unittest
from datetime import date, timedelta

from prescription import Prescription


def days_ago(days):
    return date.today() - timedelta(days=days)


class TestPrescription(unittest.TestCase):
    
    def test_days_taken_excludes_future_dates(self):
        prescription = Prescription("Codeine",
                                    dispense_date = days_ago(days=2),
                                    days_supply=4)
        self.assertListEqual([days_ago(2), days_ago(1)],
                             list(prescription.days_taken()))
#with this unit test we get a failure form the pateint class as well in that it cant use future dates, showing how changes to a single unit test can affect other unit tests in a way that might not have otherwise been noticeable. This is a way that integration testing can be done to see cross testing between units.