import sys

from ed_ui_gtk4.el_decko import ElDecko

VERSION = "2022.12.28"


def run():
    app = ElDecko(application_id="de.zray.eldecko")
    app.run(sys.argv)
