# Macropad by Jannis

A fully custom-built 9-key macropad based on the **Seeed XIAO RP2040** – including a self-designed PCB, 3D-printed enclosure, and custom firmware using KMK.  
This project is based on a complete DIY blueprint from https://blueprint.hackclub.com/home and has been individually expanded and refined.

---


## Schematic
The schematic was designed in **KiCad** and includes all core components of the macropad
<img width="1000" height="519" alt="Screenshot 2025-12-13 at 21 06 17" src="https://github.com/user-attachments/assets/226a84e8-ab6b-4529-8195-6b597e0a23d6" />

## PCB
Based on the schematic, the PCB was carefully laid out to ensure reliable routing, clean signal paths, and easy assembly.  
Special attention was given to switch alignment, component placement, and USB accessibility for the XIAO RP2040.  
<img width="497" height="667" alt="Screenshot 2025-12-13 at 21 12 02" src="https://github.com/user-attachments/assets/3abeb14a-a4a1-47e7-8444-d8cd4df8d9e2" />

## CAD
The enclosure for this macropad was designed in **Autodesk Fusion 360**.

The case consists of a **two-part design** (top plate and bottom housing) and was specifically modeled to fit the custom PCB, switches, and the Seeed XIAO RP2040.  
Clearances were carefully adjusted to ensure proper USB access, switch stability, and enough space for wiring and RGB LEDs.

The top plate is based on a DXF generated from the keyboard layout, ensuring accurate switch positioning.
The bottom case includes mounting holes for screws and heat-set inserts, making the enclosure sturdy and easy to assemble.

All CAD files are intended for **3D printing** and can be modified to fit different layouts or components if needed.
<img width="1239" height="580" alt="Screenshot 2025-12-13 at 21 14 16" src="https://github.com/user-attachments/assets/eba230bb-aa71-4162-b73b-2b36e414080c" />



## BOM
| Item | Quantity | Description |
|-----:|---------:|------------|
| Microcontroller | 1 | Seeed Studio XIAO RP2040 |
| Mechanical Switches | 9 | MX-style mechanical switches |
| Keycaps | 9 | DSA keycaps |
| RGB LEDs | 2 | SK6812 MINI-E (addressable RGB LEDs) |
| Diodes | 9 | 1N4148 through-hole diodes |
| Screws | 4 | M3 × 16 mm screws |
| Heat-set Inserts | 4 | M3 × 5 mm × 4 mm |
| PCB | 1 | Custom-designed PCB (KiCad) |
| Case (Top) | 1 | 3D-printed top plate |
| Case (Bottom) | 1 | 3D-printed bottom housing |
| USB Cable | 1 | USB-C cable (for XIAO RP2040) |



---

