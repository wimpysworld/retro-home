<h1 align="center">
 <img src=".github/logo.png" alt="Ubuntu Retro Remix Logo" width="256" />
  <br />
  Ubuntu Retro Remix Image Builder
</h1>

<p align="center"><b>Build Raspberry Pi images of Ubuntu for retro gaming</b></p>
<!-- <div align="center"><img src=".github/screenshot.jpg" alt="Ubuntu Retro Remix Screenshot" /></div> -->
<p align="center">Made with 💝 for <img src=".github/ubuntu.png" align="top" width="18" /></p>

## Introduction

A script that build Raspberry Pi images of Ubuntu for retro gaming.

We have a Discord for this project: [![Discord](https://img.shields.io/discord/712850672223125565?color=0C306A&label=WimpysWorld%20Discord&logo=Discord&logoColor=ffffff&style=flat-square)](https://discord.gg/GeHJGD9)

[![Ubuntu Retro Remix - Working hardware acceleration!](https://img.youtube.com/vi/aEUt5s4127c/0.jpg)](https://www.youtube.com/watch?v=aEUt5s4127c)

## Installation

  * Clone this project to an Intel 64-bit Ubuntu workstation.
    * `git clone https://github.com/wimpysworld/ubuntu-retro-remix.git`
  * Download the armhf [Ubuntu Server 20.04 pre-installed image for Raspberry Pi](https://ubuntu.com/download/raspberry-pi) into the project directory.

### Usage

```
Usage
  sudo ./ubuntu-retro-remix-image --remix <targetdevice> --img ubuntu-20.04-preinstalled-server-armhf+raspi.img

Available supported devices are:
  raspi
  megapi
  nespi
  superpi
```

## TODO

Pretty much everything.

## Notes

While researching RetroArch this useful information was discovered.

  * https://gist.github.com/AlexMax/32e5d038a66ce57253e740ea75736805

## Cores

  * nestopia
  * zsnes or bsnes, but not zsnes next
