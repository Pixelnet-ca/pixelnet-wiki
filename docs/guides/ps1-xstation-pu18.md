# PlayStation: installing the XStation (PU-18 board)

The **XStation** is an optical drive emulator (ODE): it takes the place of the PlayStation's disc drive, and games load from a **microSD card**. Faster loading, no more worn-out laser, and your whole library in one console.

!!! warning "This guide is for PU-18 boards only"
    The install changes with the **motherboard revision**. On a **PU-18**, there's an extra step that other boards don't need: you have to **lift 8 legs** of the Sony **CXD2545Q** chip (IC701). On a PU-8, follow the XStation guide for that board. PU-20, PU-22, PU-23 and the PSone (PM-41) are **not compatible**.

## Compatibility

| Board | Typical models | XStation |
|---|---|---|
| **PU-18** | All SCPH-5xxx (5501, 5001…), very rarely SCPH-7001 to 7003 | ✅ This guide |
| **PU-8** (early or late) | SCPH-100x, most SCPH-3xxx | ✅ Other guide (different steps) |
| **PU-20**, **PU-22**, **PU-23** | Most SCPH-7xxx, SCPH-750x, SCPH-900x | ❌ |
| **PM-41** | PSone (SCPH-10x) | ❌ |

## Identify your board

Open the console: the revision (**PU-18**, **PU-8**…) is printed on the motherboard. The model number (SCPH-…) on the label under the console gives a good first hint, but only the board itself is certain.

## What you need

- The **XStation** kit: main board, **QSB** (Quick Solder Board) for PU-18, flex cable and spacers
- A fine-tip, temperature-controlled soldering iron, flux, fine solder and solder wick
- A **fine needle** or a hobby knife (X-Acto) to lift the legs
- **Magnification** (loupe, headset or microscope): the IC701 legs are tiny
- A multimeter, tweezers, isopropyl alcohol
- A microSD card for your games

## Steps

!!! danger "Before you start"
    Unplug the power cord and **disconnect every cable from the power supply**. You have to take the PlayStation apart completely to reach the motherboard.

### 1. Find IC701 (CXD2545Q)

On the **top side** of the motherboard, find **IC701**, the Sony chip marked **CXD2545Q**, in the lower right corner.

### 2. Lift 8 legs of IC701

This is the delicate part. Lift **only** these legs: **45, 46, 47, 56, 74, 77, 78 and 80**.

For each leg: add a little flux, touch the leg with the soldering tip to melt the solder, and **gently** lift it from underneath with the needle or blade. Work one leg at a time, under magnification. Turning the board around can give you a better angle.

!!! tip "Check every leg"
    Each lifted leg must be **completely** free: no contact with its pad or the board. Check them one by one under magnification (and with the multimeter if in doubt). Lift no other legs.

### 3. Prepare the underside for the QSB

Turn the board **bottom side up**. The QSB goes in the area shown in the XStation guide. Before soldering, **lightly scratch** the via pads on the left and right of that area so solder takes properly.

### 4. Solder the QSB

Place the QSB on its pads (the markings on the QSB help with alignment) and solder it.

### 5. Remove the resistor and connect APLL

Desolder and remove the **small resistor next to the oscillator** marked **V67.737 KDS** (see the official guide for its exact position). Then connect the QSB's **APLL** pad to the point shown just above the removed resistor.

### 6. Prepare the case

On the **bottom half** of the case, cut off the **small plastic pin** marked in the XStation guide. If you skip it, the flex cable can break when you close the console.

### 7. Connect and route the flex cable

Plug the flex cable into the QSB connector, **blue side up**, and close the latch. Route the cable out through the **slot in the top shield**.

### 8. Mount the XStation

Push the **3 spacers** into the XStation board (lower right, upper right and upper left corners, seen from above). Connect the other end of the flex cable to the XStation, fold it as shown in the guide, then mount the XStation on the **posts of the original disc drive**.

### 9. Test before closing

Put the console back together far enough to power it on, insert the microSD card with a game and check that the menu appears and the game starts. Then reassemble the PlayStation.

## Official XStation guide

The steps above summarize the official guide, which has a photo for every step (pin positions, QSB location, the resistor to remove). Keep it open during the install.

[Official XStation PU-18 guide :material-open-in-new:](https://github.com/x-station/xstation-releases/wiki/xStation-ODE-installation-guide-for-the-PU-18-Playstation-1-motherboard){ .md-button target=_blank }

## Result

Your PlayStation boots into the XStation menu, and every game loads from the microSD card. The original disc drive is no longer needed: keep it in a safe place in case you ever want to go back.

Not comfortable lifting chip legs? PixelNet can [install it for you](https://pixelnet.ca/collections/installation). Questions: [support@pixelnet.ca](mailto:support@pixelnet.ca)
