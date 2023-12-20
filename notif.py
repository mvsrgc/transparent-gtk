import gi.repository.GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
 
def notifications(bus, message):
    print(f"Title: {message.get_args_list()[3]}")
    print(f"Body: {message.get_args_list()[4]}")
 
DBusGMainLoop(set_as_default=True)
 
bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)
 
mainloop = gi.repository.GLib.MainLoop()
mainloop.run()