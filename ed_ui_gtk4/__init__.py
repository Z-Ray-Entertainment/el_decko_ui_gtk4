import sys

from ed_ui_gtk4.el_decko_gtk4 import ElDecko

VERSION = "2023.5.11"


def run():
    ElDecko(application_id="de.zray.eldecko").run(sys.argv)
