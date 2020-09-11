Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ssd1306/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ssd1306/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/actions/
    :alt: Build Status

Adafruit CircuitPython driver for SSD1306 or SSD1305 OLED displays. Note that SSD1305 displays are back compatible so they can be used in-place of SSD1306 with the same code and commands.

This driver implements the `adafruit_framebuf interface <https://circuitpython.readthedocs.io/projects/framebuf/en/latest/>`__. It is **not** the `displayio` driver for the SSD1306. See the `Adafruit CircuitPython DisplayIO SSD1306 <https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306/>`_ driver for `displayio` support.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Adafruit framebuf <https://github.com/adafruit/Adafruit_CircuitPython_framebuf>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-ssd1306/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-ssd1306

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-ssd1306

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-ssd1306

Usage Example
=============

.. code-block:: python3

  # Basic example of clearing and drawing pixels on a SSD1306 OLED display.
  # This example and library is meant to work with Adafruit CircuitPython API.
  # Author: Tony DiCola
  # License: Public Domain

  # Import all board pins.
  from board import SCL, SDA
  import busio

  # Import the SSD1306 module.
  import adafruit_ssd1306


  # Create the I2C interface.
  i2c = busio.I2C(SCL, SDA)

  # Create the SSD1306 OLED class.
  # The first two parameters are the pixel width and pixel height.  Change these
  # to the right size for your display!
  display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
  # Alternatively you can change the I2C address of the device with an addr parameter:
  #display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

  # Clear the display.  Always call show after changing pixels to make the display
  # update visible!
  display.fill(0)

  display.show()

  # Set a pixel in the origin 0,0 position.
  display.pixel(0, 0, 1)
  # Set a pixel in the middle 64, 16 position.
  display.pixel(64, 16, 1)
  # Set a pixel in the opposite 127, 31 position.
  display.pixel(127, 31, 1)
  display.show()

More examples and details can be found in the `adafruit_framebuf docs <https://circuitpython.readthedocs.io/projects/framebuf/en/latest>`__.


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/adafruit_CircuitPython_SSD1306/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
