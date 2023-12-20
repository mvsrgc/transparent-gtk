import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class TransparentWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Transparent Window")
        self.set_default_size(1920, 1080)
        self.set_decorated(False)

        # Make the window background transparent
        self.set_opacity(0.8)  # Set opacity level (0.0 transparent, 1.0 opaque)

        # Add a label or other widgets here
        label = Gtk.Label(label="Hello, transparent world!")
        self.set_child(label)

class MyApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.example.transparentwindow")

    def do_activate(self):
        win = TransparentWindow(self)
        win.present()

app = MyApp()
app.run(None)

