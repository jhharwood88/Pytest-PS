from unittest.mock import Mock

from alarm import Alarm
from sensor import Sensor

#these 'test doubles' are a universal term for spies, stubs, and mocks

def test_alarm_is_off_by_default():
    alarm = Alarm()
    assert not alarm.is_alarm_on
    # this is to call the constructor and makes sure nothing is broken

class StubSensor:
    def sample_pressure(self):
        return 15


def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor=StubSensor())
    alarm.check()
    assert alarm.is_alarm_on
    #this is useing a stub to test the alarm function for a low pressure sensor, this selects the stubsensor value in place of the real sensor value

def test_normal_pressure_alarm_stays_off():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 18
    alarm = Alarm(stub_sensor)
    alarm.check()
    assert not alarm.is_alarm_on
    # this will not actiavte the alarm if a tire has normal pressure, making use of the mock framework that comes with the unit testing module in python. This will give the return value to give when testing, passing in the stub sensor instead of the real sensor.

    #these stubs are not real objects but simply simulate the object and gives hardcoded results that are easier to manage

