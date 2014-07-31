# Copyright (C) Ivan Kravets <me@ikravets.com>
# See LICENSE for details.

from os.path import join

from platformio.platforms.base import BasePlatform


class Timsp430Platform(BasePlatform):
    """
        An embedded platform for TI MSP430 microcontrollers
        (with Energia Framework)
    """

    PACKAGES = {

        "toolchain-timsp430": {
            "path": join("tools", "toolchain"),
            "alias": "toolchain",
            "default": True
        },

        "tool-mspdebug": {
            "path": join("tools", "mspdebug"),
            "alias": "uploader",
            "default": True
        },

        "framework-energiamsp430": {
            "path": join("frameworks", "energia"),
            "default": True
        }
    }

    def get_name(self):
        return "timsp430"
