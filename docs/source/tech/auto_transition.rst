auto_transition.py
====================

Define the transition between different waveguide type.

In Wuyue SP90 PDK, a linear taper will be added between two same type of waveguides with different width. The ``SLOPE`` of taper is default to be 0.2.

For the connection between different waveguide types, fixed black box transitions have been configured by default. These transitions are provided by **WUYUE**, and will be added automatically when auto-routing is called for different waveguide types.

Users are allowed to define the taper and transition, and set ``DEFAULT`` to their own specific transition policy. Please see ``gpdk > components > transition`` for more examples.