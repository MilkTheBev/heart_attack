####################################################
#                                                  #
#   heart_attack.py                                #
#                                                  #
#   as it is actually called...                    #
#                                                  #
#   A nice little tty screensaver made in python   #
#                                                  #
####################################################
import os, time, random, sys


x = True        # Will be used for looping
opr = " + "
if sys.stdout.isatty():
    cols = os.get_terminal_size().columns       # Defines the number of columns
    ttymode = True
else:
    cols = 80           # If not a tty, 80 is assumed to be the number of columns
    ttymode = False
if cols % 2 == 0:
    num2 = 2
elif cols % 2 != 0:
    num2 = 1
num = num2
btxt = ["·", "=", "-", "0", "░"]        # Character list that will print as background
ftxt = ["•", "#", "—", "1", "▓"]        # Character list that will print as foreground
btxtm = ""                              # A character selected from btxt, right now an empty string
ftxtm = ""                              # A character selected from ftxt, right now an empty string
bcolor = [
        "\033[31m", # Red
        "\033[32m", # Green
        "\033[33m", # Yellow
        "\033[34m", # Blue
        "\033[35m", # Purple
        "\033[36m", # Cyan
]
fcolor = [
        "\033[91m", # Bright red
        "\033[92m", # Bright green
        "\033[93m", # Bright yellow
        "\033[94m", # Bright blue
        "\033[95m", # Bright purple
        "\033[96m", # Bright cyan
]

# ^^ The color list used for coloring ^^


bcolorm = ""        # Background color selected from bcolor, right now empty, will remain empty if ttymode == False
fcolorm = ""        # Background color selected from fcolor, right now empty, will remain empty if ttymode == False
if ttymode:
    endchar = "\n"
elif not ttymode:
    endchar = "\r"

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")      # Detects the os environment its running on and clears the screen

lins = []                   # Will store the lines the program prints without color...

try:
    if ttymode:
        print("Press Ctrl+C to quit.\n\n")
        time.sleep(1)
    while x:
        lin = ftxtm * num                                           # Multiplies the selected foreground character with the number...
        gap = btxtm * ((cols - len(lin)) // 2)                      # Centers lin and fills the extra space with the background character
        gap2 = gap + (btxtm * (cols - len(gap + lin + gap)))                    # If any space still remains, fills it up with the background character
        print(bcolorm + gap + fcolorm + lin + bcolorm + gap2, end=endchar)       # Prints the output and colors as necessary
        lins.append(gap + lin + gap2)
        time.sleep(0.0625)      # Waits 1/16th of a second
        if num == cols:
            opr = " - "         # If the number of foreground characters is the same as the number of columns, operation becomes subtraction
        elif num == num2:
            n = random.randint(0, (len(btxt) - 1))          # Changes the foreground and background characters
            # n = 4
            cbn = random.randint(0, (len(bcolor) - 1))      # Changes background character color
            cfn = random.randint(0, (len(fcolor) - 1))      # Changes foreground character color
            opr = " + "         # Changes operation to addition if the number of foreground characters are the lowest that they can be...
            btxtm = btxt[n]
            ftxtm = ftxt[n]     # Applies changed characters
            if ttymode:
                bcolorm = bcolor[cbn]
                fcolorm = fcolor[cfn]       # Applies changed colors
            elif not ttymode:
                bcolorm = ""
                fcolorm = ""
        exec("num = num" + opr + "2")       # Controls the number of forground characters, further controlled by the operator variable opr
except KeyboardInterrupt:                                           # Executes when Ctrl+C is pressed at anytime
    if ttymode:
        print("\033[0m")
        txt_confirm = input("Save last 1000 lines to txt? (y/n): ")      # Already very self-explanatory. Asks the user for saving output to a txt file
        if txt_confirm == "y":
            with open("output.txt", "wt") as f:
                f.write("")
                f.close()       # Creates a file output.txt with nothing written...
            with open("output.txt", "at") as f:
                if len(lins) < 1000:
                    for i in range(0, (len(lins) - 1)):
                        f.write(lins[i] + "\n")                 # If length of lins is below 1000 it will save all of it in the txt file
                elif len(lins) >= 1000:
                    for i in range((len(lins) - 1001), (len(lins) - 1)):         # If its greater than 1000 it will save the last 1000 lines to the txt file
                        f.write(lins[i] + "\n")
                f.close()
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
