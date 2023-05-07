import sys

from ed_ui_gtk4.el_decko_gtk4 import ElDecko
from importlib.metadata import entry_points

VERSION = "2023.5.7"


def run():
    app = ElDecko(application_id="de.zray.eldecko")
    app.run(sys.argv)
    # core = entry_points(group='eldecko.core')
    # run_core = core["start"].load()
    # run_core()
