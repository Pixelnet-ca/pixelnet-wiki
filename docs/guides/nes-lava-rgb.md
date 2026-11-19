# NES: installing the Lava RGB 2.0

From the factory, the NES front-loader only outputs composite and RF: a soft, smeared picture. The **Lava RGB 2.0** board taps the video chip (PPU) directly and gives you **RGB, S-Video and clean composite**, plus 8 colour palettes and an in-game reset.

!!! warning "Advanced install"
    You have to **remove the PPU** (40 pins) and the **original power/A/V module** from the motherboard. You need a good desoldering tool and some patience. Not comfortable? PixelNet can [install it for you](https://pixelnet.ca/products/lava-rgb-nes).

!!! info "Sources"
    This guide is based on the instructions that come with the kit and on a [detailed public build log](https://amaiorano.io/2025/09/03/lava-rgb.html){ target=_blank } (NES-CPU-10 board). Photos from our own installs are coming.

## What it does

- **RGB, S-Video and composite** generated straight from the PPU: no more NES composite blur.
- **8 palettes** you can switch from the controller.
- **In-game reset (IGR):** reset the game from the controller.
- A **new power/A/V module** with a DIN connector (Saturn style) replaces the original module.

## Compatibility

| Console | Compatible | Note |
|---|---|---|
| **NES-001** (front-loader, NTSC) | ✅ | This guide |
| **Famicom / AV Famicom** | ✅ | Different install: follow the kit instructions |
| NES-101 (top-loader) | ⚠️ | Not covered here |

The motherboard revision is printed on the board (for example **NES-CPU-10**).

## What you need

**Kit (Lava RGB 2.0, "NES senior VER 2.0"):**

- The Lava RGB mod board
- The replacement power/A/V module (with DIN connector)
- A 12-wire connector
- Two 20-pin headers (square pins)

**To buy separately:**

- A **40-pin DIP socket** (if you want the board to be removable, recommended)
- **Two 20-pin machined (round) pin headers**: they hold much better in the socket than the square ones in the kit
- A **NES-001 cap kit** (recommended: the capacitors are 35+ years old)
- *Optional:* a **47 kΩ** resistor for expansion audio
- *Optional:* a SNES multi-out connector + 8-wire ribbon, if you prefer a SNES RGB cable to the DIN

**Tools:** soldering iron, flux, **desoldering gun** (or a good pump), solder wick, flush cutters, multimeter.

## Two install methods

| Method | How | Pros / cons |
|---|---|---|
| **Kit instructions** | Mod board soldered **directly** to the motherboard | Simpler, but hard to remove later |
| **Socketed** (PixelNet recommendation) | Socket on the motherboard, PPU soldered **onto the mod board** | The board can be pulled out for service; needs round pin headers |

The steps below follow the **socketed** method.

## Steps

### 1. Open the console and remove the motherboard

Remove the shell screws, the cartridge slot (the "72-pin connector") and pull the motherboard out. Note the board revision.

### 2. Remove the PPU

The PPU is the 40-pin video chip. Add fresh solder and flux on every pin, then clear each pin with the desoldering gun. Pins on the large **ground plane** hold heat: add solder, wait, desolder again. When every pin moves freely, lift the PPU out without forcing it.

### 3. Remove the original power/A/V module

1. Flux the **4 large anchor pins** of the metal case and remove the solder (gun, then wick).
2. Pry off the module's metal cover.
3. From the inside, desolder the module's **5 pins**.
4. Rock the module free. **The 5 pins stay on the motherboard**: the new module solders onto them.

### 4. Lay the capacitors flat

Three capacitors on the motherboard are too tall: the mod board won't fit over them. Replace them (cap kit) and **lay them flat** before soldering. Same capacitance, voltage equal or higher, respect polarity.

### 5. Prepare the mod board

1. Solder the **40-pin socket** in place of the PPU, **notch on the same side** as the original chip.
2. Push the two **round pin headers** into the socket, long pins down.
3. Lay the mod board on top, pins through the right holes, and solder.
4. Gently rock the board out of the socket (round pins bend easily).
5. Trim any pins that would sit under the PPU with flush cutters.
6. Solder the **PPU onto the mod board**, notch aligned with the board marking.

### 6. Wire the 12-wire connector

| Wires | Goes to |
|---|---|
| **1 to 8** | Matching pads on the **new power/A/V module** (same order as the labels on both boards) |
| **RST** | The motherboard **reset line** (where the Reset button connects) |
| **CLK, DATA, LATCH** | **Player 1 controller** lines (for IGR and palettes) |

!!! warning "DATA and LATCH"
    On the motherboard side, **DATA and LATCH are swapped** compared to their order on the Lava board. Check each wire with the multimeter against the kit diagram before soldering.

### 7. Install the new power/A/V module

1. Solder a **GND** wire from the module to the motherboard ground plane.
2. Dry-fit, then solder the module onto the **5 pins** left on the motherboard.
3. Connect **5 V** to the module's **PV** pad and **audio** to the **PA** pad.
4. Optional: wire the 8-wire ribbon to a SNES multi-out connector.

### 8. First test (before closing)

Plug the mod board back into the socket and route the wires down and to the side. Connect power and controller, then test **composite + audio**, then **RGB** with the right cable.

### 9. Optional: expansion audio

To hear expansion audio (Famicom games through an adapter, some flash carts): solder a **47 kΩ resistor between pins 3 and 9** of the expansion port, under the console.

### 10. Close the console

- Put back the cartridge slot and the motherboard, careful: **the new module is held only by its 5 pins**.
- **Leave the RF shield off**: it would pinch the reset and controller wires.
- Screw the shell back on.

## Using it

| Action | Controller (player 1) |
|---|---|
| **In-game reset** | Hold **Select** ~2 s, then **A** |
| **Change palette** | Hold **Select** ~2 s, then **Up**. The palette name appears on screen |

## Troubleshooting

| Problem | Fix |
|---|---|
| A PPU pin won't come out | Add solder + flux, desolder again. Never pull |
| Grey or black screen | Check the PPU orientation and the socket pins. Check every wire with the multimeter |
| IGR not working | Check the **RST** wire and the **DATA / LATCH** order |
| A colour is missing (often green) | Try another RGB cable before blaming the install |
| Expansion audio silent | Only one 47 kΩ resistor between **pins 3 and 9**, nothing else |

[Lava RGB installation service :material-cart:](https://pixelnet.ca/products/lava-rgb-nes){ .md-button .md-button--primary }

Questions: [support@pixelnet.ca](mailto:support@pixelnet.ca)
