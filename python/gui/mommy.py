import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Mommy(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Mommy?")
        self.set_border_width(6)
        self.set_default_size(500, 500)
        mommy = Gtk.Button(label="Mommy?")
        mommy.connect("clicked", self.on_mommy_clicked)
        self.add(mommy)

    def on_mommy_clicked(self, widget):
        sorry = Sorry()
        sorry.show_all()


class Sorry(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Sorry.")
        self.set_border_width(6)
        self.set_default_size(500, 500)
        sorry = Gtk.Button(label="Sorry.")
        sorry.connect("clicked", self.on_sorry_clicked)
        self.add(sorry)

    def on_sorry_clicked(self, widget):
        Gtk.Window.close(self)


win = Mommy()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()