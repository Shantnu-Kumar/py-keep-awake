import os
import time

import pyautogui

# Safety: allows stopping via Ctrl+C even if the terminal loses focus
pyautogui.FAILSAFE = True


def keep_awake(interval_seconds=60):
    """
    Keeps the PC awake by moving the mouse 1 pixel
    back and forth at a set interval.
    """
    print(f"Keeping PC awake(Developed by - Shantnu) (activity every {interval_seconds} seconds).")
    print("Press Ctrl+C to stop.\n")

    toggle = False
    try:
        while True:
            # Move mouse 1px right/left so Windows detects activity
            if toggle:
                pyautogui.moveRel(1, 0, duration=0.1)
            else:
                pyautogui.moveRel(-1, 0, duration=0.1)
            toggle = not toggle

            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nStopped. PC can sleep normally again.")


def main():
    keep_awake(interval_seconds=60)  # simulate activity once per minute


if __name__ == "__main__":
    main()
