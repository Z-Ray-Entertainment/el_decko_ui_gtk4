# El Decko GTK4
GTK4 based user interface for [El Decko](https://github.com/Z-Ray-Entertainment/el-decko)

[![build result](https://build.opensuse.org/projects/home:VortexAcherontic:ElDecko/packages/el_decko_ui_gtk4/badge.svg?type=default)](https://build.opensuse.org/package/show/home:VortexAcherontic:ElDecko/el_decko_ui_gtk4)

**v 2023.5.8:**
![](ed_ui_gtk4/assets/el_decko_gtk4_2023_05_08.png)

## requirements
- typelib-1_0-Adw-1
- El Decko Core >= 2023.5.8
- PyGObject >= 3.42.2

## Features
- Start/Stop/Reload ed-core
- Loads and displays Elgato Stream Deck button configs
  - image_idle and label

### ToDo:
- Change actual button configuration
  - Set image
  - Set Label
  - Set Action
- Rebuild grid view upon selecting another Stream Deck
- Sidebar for button configuration
