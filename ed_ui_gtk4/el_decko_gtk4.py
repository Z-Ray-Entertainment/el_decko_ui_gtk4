import threading

import gi
import ed_core

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import GLib, Gtk, GObject, Adw
from ed_core import streamdeck


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.core_running = False

        self.set_default_size(600, 250)
        self.set_title("El Decko")

        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)

        self.cb_decks = Gtk.ComboBoxText()
        self.header.pack_start(self.cb_decks)

        self.bt_launch = Gtk.ToggleButton(label="Launch")
        self.bt_launch.connect("clicked", self.start_stop_core)
        self.header.pack_end(self.bt_launch)

        self.bt_reload = Gtk.Button(label="Reload")
        self.bt_reload.connect("clicked", self.reload_core)
        self.bt_reload.set_visible(False)
        self.header.pack_end(self.bt_reload)

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.main_box)
        self.create_button_grid()

    def start_stop_core(self, button):
        if not self.core_running:
            self.start_core()
        else:
            self.stop_core()

    def start_core(self):
        self.bt_launch.set_label("Stop")
        self.core_running = True
        self.bt_reload.set_visible(True)
        threading.Thread(target=ed_core.run, args=(False,)).start()

    def stop_core(self):
        if self.core_running:
            ed_core.stop_core()
            self.bt_reload.set_visible(False)
            self.bt_launch.set_label("Launch")
            self.core_running = False

    def reload_core(self, button):
        self.stop_core()
        self.start_core()

    def create_button_grid(self):
        if streamdeck.get_stream_decks():
            first: str = ""
            for index, deck in enumerate(streamdeck.get_stream_decks()):
                deck.open()
                if not first:
                    first = deck.get_serial_number()
                self.cb_decks.append(deck.get_serial_number(), deck.deck_type())
                rows = deck.key_layout()[0]
                columns = deck.key_layout()[1]
                for i in range(0, rows):
                    row_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                    self.main_box.append(row_box)
                    for j in range(0, columns):
                        button = Gtk.Button(label=str(i) + " | " + str(j))
                        row_box.append(button)
                deck.close()
            self.cb_decks.set_active_id(first)
        else:
            print("No Elgato Stream Deck devices found!")


class ElDecko(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)
        self.connect("shutdown", self.on_close)
        self.win = None

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

    def on_close(self, app):
        self.win.stop_core()
