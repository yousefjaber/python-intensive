from enum import Enum
from abc import ABC, abstractmethod
import random


class ConnectionState(Enum):
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"


class IDevice(ABC):

    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        pass

    @abstractmethod
    def get_serial_number(self) -> str:
        pass

    @abstractmethod
    def get_device_state(self) -> ConnectionState:
        pass
home_task_text = """
<div id='intro'>
    For the current exercise, we are going to extend our SmartHouse application 
    with a monitoring service for our SmartHouse application.
</div>

<div>
    Please find a brand new abstraction of <b>Device</b> class and use it for your devices.
    Implement all the missing methods and modify your existing methods.
    The initial state of the device should be 
    <font color="blue" style="font-style:italic">Disconnected</font>.
</div>
<br>

<div>
    Create a new service <b>SmartHouseMonitoringService</b> in <i>smart_house_monitoring_service.py</i>.
    Implement the following methods:
    <ul>
        <li>
            <b>get_all_devices_serials(self) -> list[str]</b><br>
            Should return the list of serial numbers for devices.
        </li>
        <li>
            <b>check_state(self, devices: list[Device], serial_number: str) -> ConnectionState</b><br>
            Should get the state of a device.
        </li>
    </ul>
</div>
<br>

<div>
    Update <b>SmartHouseService</b> with the following:
    <ul>
        <li>Inside <font font-weight="bold" color="#906090"><b>__init__(self)</b></font>,
            create an instance of <b>SmartHouseMonitoringService</b>.
        </li>
        <li>Inside <font font-weight="bold" color="blue"><b>start()</b></font>, 
            if a device was not connected, log this as a warning and remove it from the list. 
            Otherwise, change the device state to 
            <font color="blue" style="font-style:italic">Connected</font> 
            and log the list of connected devices.
        </li>
        <li>Inside <font font-weight="bold" color="blue"><b>stop()</b></font>, 
            when a device disconnects, log this event and change its state to 
            <font color="blue" style="font-style:italic">Disconnected</font>.
        </li>
    </ul>
</div>
<br>

<div>
    Create another device <b>Computer</b> with the method 
    <font font-weight="bold" color="blue">hibernate()</font>.
    Update the service so that if a device can hibernate, then during 
    the stop process we <font font-weight="bold" color="red">DO NOT</font> change its state, 
    but log that the device is hibernating and still connected.
</div>
"""


def html_wrap(text: str) -> str:
    """Wraps the provided text in an HTML template."""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hometask IOT Service</title>
</head>
<body>
    {text}
</body>
</html>
    """


if __name__ == "__main__":
    with open("Hometask.html", "w", encoding="utf-8") as hometask_file:
        hometask_file.write(html_wrap(home_task_text))
