# heart_attack.py - a nice little tty screensaver made in python (polybar approved)

I made this script because i wanted some sort of cool display for r/unixporn... Tbh tho this looks cooler than what i expected...

The reason its called `heart_attack.py` is because if you run it in fullscreen in a real tty, it would look like the desktop is having a heart attack.

also this is the very first script i properly commented...

**IMPORTANT**: If you are sensitive to flashing lights. Either refrain from using this, or go to line 17 and set the `ttymode` variable to `False`.

If you have any suggestions, feel free to tell me. Or if you wanna make it better or wilder, fork it... I'm not stopping you.

## Usage
If running normally, you can just type this in your terminal
```bash
python3 heart_attack.py
```
Press `Ctrl+C` to exit. From here, you can choose to save the last 1000 lines to a file called `output.txt` or not.

But if running as a polybar module, open your polybar config and paste the following
```ini
[module/heart_attack] 'replace heart_attack with anything.
type = custom/script
exec = /path/to/where/you/cloned/heart_attack.py
tail = true
```

you wont be able to save the output as a txt file.. cuz youre running it as a polybar module

## Modes
### 1. `ascending` mode
![Preview](gifs/ascending.gif)

### 2. `random` mode
![Preview](gifs/random.gif)

### 3. `descending` mode
![Preview](gifs/descending.gif)

### 4. `gay` mode
![Preview](gifs/gay.gif)

### 5. `file` mode
![Preview](gifs/file.gif)
Outputs the contents of a `.txt` file after customizing it and centering it. And the cycle repeats
