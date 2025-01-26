auto_link.py
=============

Define the auto link policies between different waveguide type.

For example:

``(type(WG.WGF.O.WIRE) >> type(WG.WGF.O.WIRE), fpt.StraightPrefer(WG.WGF.O.WIRE), fpt.BendUsing(WG.WGF.O.WIRE.BEND_CIRCULAR))``

It means that when the start and end waveguide are both ``WG.WGF.O.WIRE``, the automated waveguide type for routing will be ``WG.WGF.O.WIRE`` and an automated bend ``WG.WGF.O.WIRE.BEND_CIRCULAR`` will be added.


Users are allowed to define and set ``DEFAULT`` to their own specific linking policy.

