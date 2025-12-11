# --- Basic KMK Setup --------------------------------------------------------

import board
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

# ---------------------------------------------------------------------------

keyboard = KMKKeyboard()

# Enable Macros
macros = Macros()
keyboard.modules.append(macros)

# ---------------------------------------------------------------------------
# PIN DEFINITIONS
# ---------------------------------------------------------------------------

# ⚠️ Diese Pins bitte mit deinen echten Pins ersetzen!
SWITCH_PINS = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
    board.D7,
    board.D8,
]

# SK6812 RGB LEDs
LED_PIN = board.D9        # Data-In der 2 LEDs
NUM_LEDS = 2

pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=0.25, auto_write=True)

# ---------------------------------------------------------------------------
# KEYBOARD MATRIX
# ---------------------------------------------------------------------------

keyboard.matrix = KeysScanner(
    pins=SWITCH_PINS,
    value_when_pressed=False,
)

# ---------------------------------------------------------------------------
# LED helper — set different colors for each key
# ---------------------------------------------------------------------------

LED_COLORS = [
    (255, 0, 0),     # Key 1 → red
    (255, 128, 0),   # Key 2 → orange
    (255, 255, 0),   # Key 3 → yellow
    (0, 255, 0),     # Key 4 → green
    (0, 255, 255),   # Key 5 → cyan
    (0, 0, 255),     # Key 6 → blue
    (128, 0, 255),   # Key 7 → purple
    (255, 0, 128),   # Key 8 → magenta
    (255, 255, 255), # Key 9 → white
]

def set_led_color_for_key(index):
    color = LED_COLORS[index % len(LED_COLORS)]
    pixels[0] = color
    pixels[1] = color


# ---------------------------------------------------------------------------
# KEYMAP (9 Taster = 1 Reihe mit 9 Elementen)
# ---------------------------------------------------------------------------

keyboard.keymap = [
    [
        KC.A,                                 # Key 1
        KC.B,                                 # Key 2
        KC.C,                                 # Key 3
        KC.DELETE,                            # Key 4
        KC.MACRO("Hello World!"),             # Key 5
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),  # Key 6
        KC.ENTER,                             # Key 7
        KC.SPACE,                             # Key 8
        KC.ESC,                               # Key 9
    ]
]

# ---------------------------------------------------------------------------
# HOOK: LED update whenever a key is pressed
# ---------------------------------------------------------------------------

def before_press(key, *args, **kwargs):
    set_led_color_for_key(key)

macros.before_press = before_press

# ---------------------------------------------------------------------------
# START KEYBOARD
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    keyboard.go()

