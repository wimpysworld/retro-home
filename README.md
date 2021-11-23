<h1 align="center">
 <img src=".github/logo.png" alt="Retro Home Logo" width="256" />
  <br />
  Retro Home
</h1>

<p align="center"><b>Your Home for Retro Gaming</b></p>
<!-- <div align="center"><img src=".github/screenshot.jpg" alt="Retro Home Screenshot" /></div> -->
<p align="center">Made with 💝 for <img src=".github/ubuntu.png" align="top" width="18" /></p>

## Introduction

**Retro Home is your home for retro gaming 🕹**

Retro Home is made possible thanks to [Ludo](https://ludo.libretro.com/).

> Ludo is a minimalist frontend for emulators

This repository hosts the script that builds Retro Home images for Raspberry Pi
devices and the associated documentation to help get you retro gaming in style.

We have a Discord for this project: [![Discord](https://img.shields.io/discord/712850672223125565?color=0C306A&label=WimpysWorld%20Discord&logo=Discord&logoColor=ffffff&style=flat-square)](https://discord.gg/GeHJGD9)

### Features

  * Optimized images for Raspberry Pi 2, 3 and 4.
  * Based on [Ubuntu](https://ubuntu.com) and [Ludo](https://ludo.libretro.com/)
  * [Supported emulation](https://jean-andre-santoni.gitbook.io/ludo/emulated-consoles):
    * Arcade
​​    * Atari 2600
    * Atari 5200
    * Atari 7800
    * Atari Jaguar
    * Atari Lynx
​​    * Game Boy
    * Game Boy Color
    * Game Boy Advance
    * Magnavox Odyssey2
    * Microsoft MSX
    * Microsoft MSX2
    * Neo Geo Pocket
    * Neo Geo Pocket Color
    * Nintendo Entertainment System
    * Super Nintendo Entertainment System
    * Nintendo 64 (Experimental)
    * Nintendo DS
​​    * Nintendo Pokémon Mini
    * Nintendo Virtual Boy
    * Sega 32X
    * Sega Game Gear
    * Sega Genesis / Megadrive
    * Sega Master System
    * Sega Mega CD
    * Sega PICO
​​    * Sega Saturn
    * PC Engine
    * PC Engine CD
    * PC Engine SuperGrafx
    * PC-FX
​​    * PC-98
    * Sony PlayStation
    * Vectrex
    * Wonder Swan
    * Wonder Swan Color
  * Supported Raspberry Pi:
    * Raspberry Pi 2 Model B
    * Raspberry Pi 3 Model A+
    * Raspberry Pi 3 Model B
    * Raspberry Pi 3 Model B+
    * Raspberry Pi 4 Model B  (**Recommended**)
    * Raspberry Pi 400
    * Raspberry Pi Zero 2 W
  * Automatic first boot file system expansion
  * WiFi and Bluetooth management
  * Integrated Samba and SSH server for copying over ROMS
  * Optional *micro desktop*, based on [GNOME Flashback](https://wiki.gnome.org/Projects/GnomeFlashback)

## Downloads

  * *"Coming soon..."*

No, really. It will be soon. We're just working through some testing to satisfy
ourselves the first alpha images are ready for wider evaluation.

### Putting Ludo on a Raspberry Pi

  * tbd

## Building Images

  * Clone the Retro Home project
    * `git clone https://github.com/wimpysworld/retro-home.git`

It is best to run the `retro-home-image` on an Ubuntu 20.04 x86 64-bit
workstation, ideally running in a VM via [Quickemu](https://github.com/quickemu-project/quickemu)

This following will build a Retro Home armhf image for Raspberry Pi.

```bash
sudo ./retro-home-image --device raspi
```

You can tweak some variable towards the bottom of the `retro-home-image` script.
However, **Ludo currently only publishes pre-built binaries for `armhf`**, so
changing the target architecture is not recommended.

```bash
IMG_VER="21.10"
IMG_RELEASE="impish"
IMG_ARCH="armhf"
```

You can also create a build without the desktop environment by setting
`SKIP_DESKTOP` to `1` in the variables near the end of the `retro-home-image`
script.

```bash
# Set to 1 to skip installing these components
SKIP_LUDO=0
SKIP_DESKTOP=1
SKIP_UBUNTU_STANDARD=0
```

### Usage

We will be adding hardware support for various retro themed Raspberry Pi cases
in the future.

```
Usage
  sudo ./retro-home-image --device <targetdevice>

Available supported devices are:
  raspi
  megapi
  nespi
  superpi
```

## FAQ

### How do I put ROMs on Retro Home?

ROMs are stored in `/storage/Retro/roms` on the Retro Home file system. Once
you've copied some ROMs to Retro Home (see below) you can use Ludo to
[scan your games](https://jean-andre-santoni.gitbook.io/ludo/launching-games).

If Retro Home has an active Internet connection while scanning your games, game
thumbnails will be automatically be downloaded. Thumbnails are stored
persistently and are usable without an Internet connection.

**Copying ROMs on to a Raspberry Pi via WiFi is extremely slow 🐢 We highly
recommend you use wired Ethernet for copying files over the network to Retro
Home.**

#### Windows File Sharing (Samba)

Connect to Retro Home via Windows File Sharing (Samba) and copy ROMs to the
*ROMs* folder.

#### Secure Shell (SSH)

Example:

```bash
scp *.zip ludo@retro-home-raspi.local:Retro/roms/
```

#### File copy

If you have a Linux workstation, you can insert the Retro Home
memory card / USB stick into an appropriate reader and copy ROMs to the
partition labelled `writable` in the `/storage/Retro/roms` directory.

### What is the default username and password:

This is the default username and password for logging into Retro Home via SSH
or the desktop.

  * Username: `ludo`
  * Password: `retro`

### Why is a desktop environment bundled?

Having a small desktop environment is helpful during the early stages of
development and debugging.

We will continue to include the desktop environment in most of the Retro Home
images we make available as it is useful for downloading and installing your
ROMs if you don't have another computer available.

We won't be including the desktop on Retro Home images targeting handheld
devices.

### What is included in the desktop environment?

  * Archive Manager
  * BitTorrent Client
  * File Manager
  * Ludo
  * Network Manager
  * Terminal Emulator
  * Text Editor

### How do I access the desktop?

**You must have a keyboard and mouse connected to Retro Home to access the desktop.**

  * Boot Retro Home and when Ludo has loaded pressed the Escape key.
  * Ludo will exit and you'll be presented with the display manager.
  * Select the *GNOME FlashBack* session by clicking the icon above the password entry.
  * Enter the password for the Ludo user (`retro` is the default password) and press Enter.

To shutdown or reboot Retro Home from the desktop environment, click the cog
icon in the top right of the panel.
