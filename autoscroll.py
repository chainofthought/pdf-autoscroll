"""
PDF Auto-Scroller for reading/studying in Microsoft Edge (or any window).

Setup (one time):
    pip install pyautogui keyboard

Usage:
    1. Run:  python pdf_autoscroll.py
    2. Open your PDF in Edge.
    3. Keep the MOUSE POINTER over the PDF (scroll events go to the window
       under the pointer), then press S to start.

Hotkeys (letters; they work while Edge is focused):
    S  -> Start / Pause scrolling
    F  -> Faster
    L  -> Slower
    R  -> Reverse direction (scroll up to re-read, press again to go down)
    Q  -> Quit the script

Note: while the script runs, these letters are captured by the script and
won't type anywhere else. Quit with Q when you're done.
"""

import time
import threading

import keyboard
import pyautogui

# ---------------- Settings you can tweak ----------------
START_SPEED = 40      # pixels per second (gentle reading pace)
MIN_SPEED = 5
MAX_SPEED = 300
SPEED_STEP = 5        # how much F / L change the speed
TICK = 0.02           # loop check interval in seconds
CHUNK = 120           # wheel units per scroll event (120 = one mouse notch).
                      # Lower (e.g. 40) = smoother, but some apps ignore tiny values.
# --------------------------------------------------------

UNITS_PER_PIXEL = 1.2  # ~120 wheel units per 100 px in a browser

state = {
    "running": False,
    "speed": START_SPEED,
    "direction": -1,   # -1 = down, +1 = up
    "quit": False,
}

pyautogui.FAILSAFE = False


def show_state() -> None:
    mode = "SCROLLING" if state["running"] else "PAUSED"
    arrow = "down" if state["direction"] < 0 else "up"
    msg = f"[{mode}] speed: {state['speed']} px/s  direction: {arrow}"
    print(f"\r{msg:<60}", end="", flush=True)


def toggle() -> None:
    state["running"] = not state["running"]
    show_state()


def faster() -> None:
    state["speed"] = min(MAX_SPEED, state["speed"] + SPEED_STEP)
    show_state()


def slower() -> None:
    state["speed"] = max(MIN_SPEED, state["speed"] - SPEED_STEP)
    show_state()


def reverse() -> None:
    state["direction"] *= -1
    show_state()


def quit_script() -> None:
    state["quit"] = True


def scroll_loop() -> None:
    carry = 0.0
    last = time.perf_counter()
    while not state["quit"]:
        time.sleep(TICK)
        now = time.perf_counter()
        elapsed = now - last
        last = now

        if not state["running"]:
            carry = 0.0
            continue

        carry += state["speed"] * elapsed * UNITS_PER_PIXEL
        if carry >= CHUNK:
            carry -= CHUNK
            pyautogui.scroll(state["direction"] * CHUNK)


def main() -> None:
    keyboard.add_hotkey("s", toggle, suppress=True)
    keyboard.add_hotkey("f", faster, suppress=True)
    keyboard.add_hotkey("l", slower, suppress=True)
    keyboard.add_hotkey("r", reverse, suppress=True)
    keyboard.add_hotkey("q", quit_script, suppress=True)

    print(__doc__)
    show_state()

    threading.Thread(target=scroll_loop, daemon=True).start()

    try:
        while not state["quit"]:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    keyboard.unhook_all()
    print("\nStopped.")


if __name__ == "__main__":
    main()