# ☕ py-keep-awake

A lightweight Python script that keeps your Windows PC awake by simulating
mouse activity. Perfect for long downloads, remote work, presentations,
or when you just don't want your machine locking itself every 5 minutes.

## ✨ Features

- 🖱️ Simulates a 1-pixel mouse jiggle — invisible & non-intrusive
- 🔓 Works **without admin rights**
- ⚙️ Adjustable interval (default: once per minute)
- 🛑 Clean exit with `Ctrl+C` — no leftover processes
- 📜 Bonus: opens the on-screen virtual keyboard (optional module)

## 📦 Installation

```bash
git clone https://github.com/yourusername/py-keep-awake.git

Install dependency:
pip install pyautogui

## 🚀 Usage
python keep_awake.py
Stop it anytime with Ctrl+C.

Change the interval
keep_awake(interval_seconds=300)  # activity every 5 minutes

🧠 How it works
Windows resets its idle timer on any user input. By moving the mouse
1 pixel back and forth, the script convinces Windows that you're active —
without interfering with your work.

⚠️ Disclaimer
Use responsibly — e.g., during legitimate long-running tasks. Keeping
work machines artificially awake may violate company IT policies.
