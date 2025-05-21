# heart_attack.py - a nice little tty screensaver made in python (polybar approved)

I made this script because i wanted some sort of cool display for r/unixporn... Tbh tho this looks cooler than what i expected...

The reason its called `heart_attack.py` is because if you run it in fullscreen in a real tty, it would look like the desktop is having a heart attack.

also this is the very first script i properly commented...

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

## Screenshots
![Preview](screenshots/screenshot1.png)
![Preview](screenshots/screenshot2.png)
![Preview](screenshots/screenshot3.png)
![Preview](screenshots/screenshot4.png)
![Preview](screenshots/screenshot5.png)
