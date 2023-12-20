import gi.repository.GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Gdk, Adw
import time

# Define the function to handle notifications
def notifications(bus, message):
    args = message.get_args_list()
    app_name, notification_id, icon, summary, body, actions, hints, expire_timeout = args[:8]

    urgency = hints.get("urgency", 1)

    if summary == "LINUX SUCKS" and urgency == 1:
        # Check if this notification ID has already been processed
        # Display the full-screen alert
        win = FullScreenAlert(app)
        win.present()

# Initialize the D-Bus loop
DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)

class FullScreenAlert(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.fullscreen()

        # Layout container
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        layout.set_margin_top(50)
        layout.set_margin_bottom(50)
        layout.set_margin_start(50)
        layout.set_margin_end(50)
        self.set_child(layout)

        # Event Title
        event_title = Gtk.Label(label="Meeting with Team")
        event_title.get_style_context().add_class("h1")
        layout.append(event_title)

        # Event Time
        event_time = Gtk.Label(label="Today at 2:00 PM")
        event_time.get_style_context().add_class("h2")
        layout.append(event_time)

        # Event Location or Link
        event_location = Gtk.LinkButton(uri="https://video-call-link.com", label="Join Video Call")
        layout.append(event_location)

        # Snooze Button
        snooze_button = Gtk.Button(label="Snooze")
        snooze_button.connect("clicked", self.on_snooze_clicked)
        layout.append(snooze_button)

    def on_snooze_clicked(self, button):
        # Handle snooze functionality here
        pass

class MyApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.example.fullscreenalert")

    def do_activate(self):
        pass  # We don't need to display the initial window here

app = MyApp()

# Keep the application running
mainloop = gi.repository.GLib.MainLoop()
mainloop.run()

