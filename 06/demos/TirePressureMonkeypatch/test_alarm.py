from unittest.mock import patch, Mock

from alarm import Alarm


def test_alarm_with_high_pressure_value():
    with patch('alarm.Sensor') as test_sensor_class:
        #this call to patch will allow a refernce to the sensor class that the alarm will use
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 22
        #stub created to work as a test dobule
        test_sensor_class.return_value = test_sensor_instance
        #will return an instance of the test dobule previously created
        alarm = Alarm()
        alarm.check()

        assert alarm.is_alarm_on
        #this is to test that the alarm activates properly with the new test case

        #We use a monkeypatch to replace a stubbed version of the sensor class in real time, meaning it can still assocaite with the alarm class but will still be able to get a refernec to the test double. This can be seen in the patch('alarm.Sensor)

@patch('alarm.Sensor')
#to monkeypatch we will use a decorator to the whole test function, then we will use the test sensor class which is being monekypatched as an argument to the test case. We will then assing it to the stub, and work similarly to the one above with the exception of the decorator.
def test_alarm_with_too_low_pressure_value(test_sensor_class):
    test_sensor_instance = Mock()
    test_sensor_instance.sample_pressure.return_value = 16
    test_sensor_class.return_value = test_sensor_instance

    alarm = Alarm()
    alarm.check()

    assert alarm.is_alarm_on
