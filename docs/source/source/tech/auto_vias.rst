auto_vias.py
====================

Define the vias between different metal line type.

In Wuyue SP90 PDK, when two adjacent metal lines are connected, the corresponding vias array will be added automatically, please refer to the Process Cross Section in Chapter 2 of the Wuyue SP90 technology handbook for the specific metal stacking relationship.

Users are allowed to define vias and change related parameters by their own specific requirements. Please see ``technology > vias.py`` and ``components > via > vias.py`` to modifiy the default vias. Please note that the structure of the vias needs to follow the design rules of **WUYUE**.