#!/usr/bin/env python3


import gi
import sys
import pathlib
import shutil

img_path = sys.argv[1]
config_path = "/home/kali/.config/screenshat/conf"
last_path = pathlib.Path(config_path).read_text()

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Screenshat")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text(last_path)
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        button_save = Gtk.Button.new_with_mnemonic("_Save")
        button_save.connect("clicked", self.on_save_clicked)
        hbox.pack_start(button_save, True, True, 0)

    def on_save_clicked(self, button):
        current_path = self.entry.get_text()

        # Update config file
        pathlib.Path(config_path).write_text(current_path)
        
        # in doubt do mkdir -p new directory
        pathlib.Path(current_path).mkdir(parents=True, exist_ok=True)

        # move file 
        shutil.move(img_path, current_path)


win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

