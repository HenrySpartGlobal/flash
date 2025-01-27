import tkinter as tk
import keyboard
import time
import threading


key_for_top = "f5"
key_for_jungle = "f6"
key_for_mid = "f7"
key_for_adc = "f8"
key_for_support = "f9"

# Each role will have a name and a time_left and the hot keys for this (in seconds)
# idk why i called it champions everywhere dont ask
champions = [
    {"name": "Top", "time_left": 0, "Key": key_for_top},
    {"name": "Jungle", "time_left": 0, "Key": key_for_jungle},
    {"name": "Mid", "time_left": 0, "Key": key_for_mid},
    {"name": "ADC", "time_left": 0, "Key": key_for_adc},
    {"name": "Support", "time_left": 0, "Key": key_for_support},
]

# Map hotkeys to the index in 'champions' dict
# change the key binds at the very top if you don't like the hot keys
hotkey_to_index = {
    key_for_top: 0,
    key_for_jungle: 1,
    key_for_mid: 2,
    key_for_adc: 3,
    key_for_support: 4,
}

COOLDOWN = 300  # 5 minutes in seconds 5head

def start_flash_timer(index):
    """Reset the flash timer for champion at 'index' to 5 minutes."""
    champions[index]["time_left"] = COOLDOWN

# Create the main Tkinter window
root = tk.Tk()
root.title("LoL Flash Timers")

# So the app is always ontop of anything u have open
root.attributes('-topmost', True)
root.lift()


# Create a frame to hold champion labels
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# We'll store one label per champion so we can update them
labels = []

for i, champ in enumerate(champions):
    row_frame = tk.Frame(frame)
    row_frame.pack(anchor="w")

    # Champion Name Label
    name_label = tk.Label(row_frame, text=f"{champ['name']} ({champ['Key']})", width=15, anchor="w")
    name_label.pack(side=tk.LEFT, padx=5)

    # Timer Label
    timer_label = tk.Label(row_frame, text="Ready", width=10, anchor="e")
    timer_label.pack(side=tk.LEFT, padx=5)

    labels.append(timer_label)

def refresh_labels():
    """Refresh each label to display the current time left or 'Ready'."""
    for i, champ in enumerate(champions):
        time_left = champ["time_left"]
        if time_left > 0:
            m = time_left // 60
            s = time_left % 60
            labels[i].config(text=f"{m:01d}:{s:02d}", fg="red")
        else:
            labels[i].config(text="Ready", fg="green")

def update_timers():
    """Background thread that decrements time_left every second."""
    while True:
        for champ in champions:
            if champ["time_left"] > 0:
                champ["time_left"] -= 1

        # update GUI
        root.after(0, refresh_labels)
        time.sleep(1)

# Setup global hotkeys
def setup_hotkeys():
    for hk, idx in hotkey_to_index.items():
        keyboard.on_press_key(hk, lambda e, i=idx: start_flash_timer(i))

setup_hotkeys()

# Start a background thread that updates the timers
t = threading.Thread(target=update_timers, daemon=True)
t.start()

# Start the Tkinter event loop
root.mainloop()
