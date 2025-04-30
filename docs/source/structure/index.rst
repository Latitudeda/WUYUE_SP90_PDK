PDK structure
======================

Process Design Kit (PDK) is a tool for designated users to generate circuit layouts based on Wuyue SP90 design rules and technology settings.

``Wuyue_SP90_V0p7_Latitudeda`` package includes three subfolders: ``components``, ``examples``, and ``technology``.

* ``components``

    * Fixed cells: All fixed cells, including ``BB Edge Coupler``, ``BB Grating Coupler``, ``BB MPD``, ``BB Doped Heater``, ``BB PNPS``, etc, are named and designed by **WUYUE** and cannot be changed.

    * Parametrized cells (PCells): Designed by **Latitudeda**, including ``Bend``, ``Straight``, ``Taper``, etc. Please see ``gpdk > components`` for more designed components by **Latitudeda**.

* ``examples``

    * ``tech_test.py`` : Tests that waveguide types, metal wire types, auto routing, and auto link function works normally under the PDK setting. Please see ``gpdk > examples`` for more circuit examples.

* ``technology``

    * Store the technology setting which matched the Wuyue SP90 design rules. We recommend users not to change the settings in technology folder.

    * See chapter ``Technology setting`` for more specific definition.

* ``Wuyue_SP90_V0p7_Latitudeda.lyp``

    * This file allows layout tools e.g. Klayout to recognize the layer information when displaying gds file to the layout tool.

    .. image:: ../images/lyp.png
