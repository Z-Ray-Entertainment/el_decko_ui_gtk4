import sys

from ed_ui_gtk4.el_decko_gtk4 import ElDecko

VERSION = "2023.5.8.2"


def run():
    app = ElDecko(application_id="de.zray.eldecko")
    app.run(sys.argv)
