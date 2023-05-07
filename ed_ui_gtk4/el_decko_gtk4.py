import gi
import ed_core

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from ed_core import streamdeck


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(600, 250)
        self.set_title("El Decko")
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        self.dd_decks = Gtk.DropDown()
        self.header.pack_start(self.dd_decks)

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.main_box)
        self.create_button_grid()

    def create_button_grid(self):
        if streamdeck.get_stream_decks():
            for index, deck in enumerate(streamdeck.get_stream_decks()):
                deck.open()
                self.dd_decks.set_list_factory()
                rows = deck.key_layout()[0]
                columns = deck.key_layout()[1]
                print("Rows: " + str(rows) + " | Columns: " + str(columns))
                for i in range(0, rows):
                    row_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                    self.main_box.append(row_box)
                    for j in range(0, columns):
                        button = Gtk.Button(label=str(i) + " | " + str(j))
                        row_box.append(button)
                deck.close()
        else:
            print("No Elgato Stream Deck devices found!")


class ElDecko(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()
