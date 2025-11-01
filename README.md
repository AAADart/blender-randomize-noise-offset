# Randomize Noise Offset (Blender Add-on)

**Graph Editor → N → Modifiers → Randomize Noise Offset**  
Randomizes the **Offset** parameter of all **NOISE** F-Curve modifiers for the active Actions of selected objects.  
The offset is defined in **seconds** (automatically converted to frames using FPS).

![Panel](assets/screenshot_panel.png)

## Features
- Works on **selected objects** (or on the active one if none are selected).  
- **Seed** for reproducibility.  
- **Offset Min/Max (s)** — range in seconds, automatically converted to frames.

## Requirements
- Blender **4.0+** (tested on 4.5)

## Installation
1. Download the release ZIP or create a ZIP from `addon/randomize_noise_offset`.  
2. In Blender: **Edit → Preferences → Add-ons → Install...** → select the ZIP → **Install**.  
3. Enable the add-on (check the box).  
4. Open **Graph Editor**, press **N**, go to the **Modifiers** tab → section **Randomize Noise Offset**.

## Usage
1. Select objects with animation (or keep one active object with an Action).  
2. Set **Seed**, **Offset Min/Max (s)**.  
3. Press **Randomize Noise Offset** — all NOISE modifiers will get a randomized offset.

## Why this add-on?
Blender doesn’t provide a built-in operator to batch randomize the Offset of NOISE modifiers.  
Without this add-on, the process must be done manually for each curve.

## Future ideas
- Option to affect only **selected F-Curves** in the Graph Editor.  
- Toggle to work in **frames** instead of seconds.  
- Filter by Action name or specific curve channels.

## Development
- Code: `addon/randomize_noise_offset/__init__.py`  
- Style: PEP8, class prefixes `RNO_` / `GRAPH_`  
- Pull requests and issues are welcome!

## License
GPL-3.0-or-later (primary license for Blender Extensions)  
MIT license also included — see [LICENSE](LICENSE).
