"""
@ Author      : Jason Hong
@ Description : Body Detector in OBLink - It obtain the body detected sensor from the obox
@ Notes:        Copy this file and place it in your
                "Home Assistant Config folder\custom_components\sensor\" folder
                You may have to install two additional packages
                ...
                The following resources are supported: sp, sp_change_pct, sp_change
                dow, dow_change_pct, dow_change, nasdaq, nasdaq_change_pct, nasdaq_change
                Check the configuration in sensor.yaml (search for onBrightLink).
"""


from homeassistant.helpers.entity import Entity

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([BodyDetectSensor()])

class BodyDetectSensor(Entity):
    @property
    def name(self):
        return 'BodyDetector'
    
    @property
    def type(self):
        return 1

    @property
    def subType(self):
        return 1
    
    @property
    def state(self):
        return '0100000000000000'

    @property
    def is_online(self):
        return True
    
    @property
    def is_detected(self):
        return True

