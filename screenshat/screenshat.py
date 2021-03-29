#!/usr/bin/env python3

# remember to change config_path to a valid path

# Usage: python screenshat.py /path/to/screenshot

# if it says PIL module not found, do pip install image

# for xfce4-screenshoter (mostly kali linux)
# i3/config: bindsym Mod1+m exec xfce4-screenshooter -r -o ~/projects/TheWizardOfEvergreenTerrace/screenshat/screenshat.py

# for flameshot
# .xinitrc: exec dbus-launch i3
# i3/config: bindsym Mod1+m exec SSHOTPATH=/tmp/$(date "+%F-%H-%M-%N").png && flameshot gui -r > "$SSHOTPATH" && python /home/giovi/Projects/TheWizardOfEvergreenTerrace/screenshat/screenshat.py "$SSHOTPATH"

import gi
import sys
import pathlib
import shutil

from PIL.PngImagePlugin import PngImageFile, PngInfo

if (len(sys.argv) != 2):
    sys.exit()

img_path = sys.argv[1]

if not pathlib.Path(img_path).is_file():
    sys.exit()

config_path = "/home/giovi/.config/screenshat/conf"

# config checks
if not pathlib.Path(config_path).is_file():
    pathlib.Path(config_path[:-4]).mkdir(parents=True, exist_ok=True)
    pathlib.Path(config_path).write_text("")

last_path = pathlib.Path(config_path).read_text()

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

# Gui window
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

        self.entryy = Gtk.Entry()
        self.entryy.set_text("")
        vbox.pack_start(self.entryy, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        button_save = Gtk.Button.new_with_mnemonic("_Save")
        button_save.connect("clicked", self.on_save_clicked)
        hbox.pack_start(button_save, True, True, 0)

    def on_save_clicked(self, button):
        current_path = self.entry.get_text()

        # write metadata
        metadata = PngInfo()
        metadata.add_text("screenshat", self.entryy.get_text())

        img = PngImageFile(img_path)
        img.save(img_path, pnginfo=metadata)
        

        # Update config file
        pathlib.Path(config_path).write_text(current_path)
        
        # in doubt do mkdir -p new directory
        pathlib.Path(current_path).mkdir(parents=True, exist_ok=True)

        # move file 
        shutil.move(img_path, current_path)

        self.destroy()


win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
