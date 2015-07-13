Web User Interface for Automate
===============================

`Automate <http://github.com/tuomas2/automate>`_ is a general purpose Python automatization library.

Automate Web UI extension provides easy to use approach to monitoring and modifying
Automate system and its components. Features:

- Displayed data updated in real time via Websocket

- Responsive design (using `Bootstrap <http://getbootstrap.com/>`_ CSS & JS library), suitable for
  mobile and desktop use.

- Optional authentication
- Read-only and read-write modes.

  - Read-only mode allows only monitoring (default)
  - Read-write mode allows modifying the System by:

    - adding new Actuators / Sensors / Programs
    - modifying existing Actuators / Sensors / Programs
    - Quick editing of user-editable sensors from main views

- HTTP and secured HTTPS servers supported (powered by built in `Tornado Web Server <www.tornadoweb.org/>`_)

See full documentation and screenshots at
`Readthedocs.org <http://python-automate.readthedocs.org/en/latest/official_extensions/webui.html>`_.

Installation
------------

Install from Pypi::

    pip install automate-webui

Optionally, you could install also by cloning GIT repository and installing manually::

    git clone https://github.com/tuomas2/automate-webui.git
    cd automate-webui
    ./setup.py install

Licence
-------

Automate is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Automate is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Automate.  If not, see http://www.gnu.org/licenses/.


