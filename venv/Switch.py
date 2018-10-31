from pyHS100 import SmartPlug, SmartBulb
from pprint import pformat as pf

# plug = SmartPlug("192.168.31.99")
# print("Hardware: %s" % pf(plug.hw_info))
# print("Full sysinfo: %s" % pf(plug.get_sysinfo())) # this prints lots of information about the device
#
#
# print("Current state: %s" % plug.state)
# plug.turn_on()
#
# print("Current time: %s" % plug.time)
#
#
# print("Current LED state: %s" % plug.led)
# plug.led = False # turn off led
# print("New LED state: %s" % plug.led)


bulb = SmartBulb("192.168.31.100")


print(bulb.brightness)
if bulb.is_dimmable:
    bulb.brightness = 100

bulb.turn_on()

#print("Hardware: %s" % pf(bulb.hw_info))
#print("Full sysinfo: %s" % pf(bulb.get_sysinfo()))  # this prints lots of information about the device
print(bulb.is_on)
