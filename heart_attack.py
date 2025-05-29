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


x = True                                                                            # Will be used for looping
opr = " + "
if sys.stdout.isatty():
    cols = os.get_terminal_size().columns                                           # Defines the number of columns
    ttymode = True                                                                  # If you are sensitive to flashing images, please set this flag to False... it disables color... and defaults to 'ascending' mode
else:
    cols = 80                                                                       # If not a tty, 80 is assumed to be the number of columns
    ttymode = False
if cols % 2 == 0:
    num2 = 2
elif cols % 2 != 0:
    num2 = 1
num = num2
btxt = ["·", "=", "-", "0", "░"]                                                    # Character list that will print as background
ftxt = ["•", "#", "—", "1", "▓"]                                                    # Character list that will print as foreground
btxtm = " "                                                                         # A character selected from btxt, right now an empty string
ftxtm = "*"                                                                         # A character selected from ftxt, right now an empty string
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
cbn = 0                                                                             # Predefining the background color index
cfn = 0                                                                             # Predefining the foreground color index

# ^^ The color list used for coloring ^^

bcolorm = ""                                                                        # Background color selected from bcolor, right now empty, will remain empty if ttymode == False
fcolorm = ""                                                                        # Foreground color selected from fcolor, right now empty, will remain empty if ttymode == False

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")                                                              # Detects the os environment its running on and clears the screen

lins = []                                                                           # Will store the lines the program prints without color...
modes = [
        "ascending",    # The first one i coded... increases the number of foreground characters until it reaches the maximum width it can, from which it begins to shrink... when it fully shrinks, a new pattern begins.
        "random",       # aka. chaos... everything is randomized after each line.... time interval, random... colors, random... characters, random...
        "descending",   # Just like the first one, but reversed... may take time....
        "gay"           # ik a bit offensive.... im sorry... it basically outputs a rainbow... each line colored differently...
]

# ^^ The different modes in which it can output ^^

for i in range(0, len(modes)):
    print(str(i + 1) + ". " + modes[i])
if ttymode:
    mode = modes[int(input("Choose mode (for example, type '1' for 'ascending' mode): ")) - 1] # Prompts the user to choose the mode... and this wont loop. So run the script again to switch mode
elif not ttymode:
    mode = "ascending"

if mode == "ascending":
    boolascending = True
    boolrandom = False
    booldescending = False
    boolgay = False
elif mode == "random":
    boolascending = False
    boolrandom = True
    booldescending = False
    boolgay = False
elif mode == "descending":
    boolascending = False
    boolrandom = False
    booldescending = True
    boolgay = False
    num = cols
elif mode == "gay":
    boolascending = False
    boolrandom = False
    booldescending = False
    boolgay = True

try:
    if ttymode:
        print("Press Ctrl+C to quit.\n\n")
        time.sleep(1)
    while x:
        lin = ftxtm * num                                                               # Multiplies the selected foreground character with the number...
        gap = btxtm * ((cols - len(lin)) // 2)                                          # Centers lin and fills the extra space with the background character
        gap2 = gap + (btxtm * (cols - len(gap + lin + gap)))                            # If any space still remains, fills it up with the background character
        print(bcolorm + gap + fcolorm + lin + bcolorm + gap2)                           # Prints the output and colors as necessary
        lins.append(gap + lin + gap2)
        if boolascending:
            time.sleep(0.0625)                                                          # Waits 1/16th of a second
            if num == cols:
                opr = " - "                                                             # If the number of foreground characters is the same as the number of columns, operation becomes subtraction
            elif num == num2:
                n = random.randint(0, (len(btxt) - 1))                                  # Changes the foreground and background characters
                cbn = random.randint(0, (len(bcolor) - 1))                              # Changes background character color
                cfn = random.randint(0, (len(fcolor) - 1))                              # Changes foreground character color
                opr = " + "                                                             # Changes operation to addition if the number of foreground characters are the lowest that they can be...
                btxtm = btxt[n]
                ftxtm = ftxt[n]                                                         # Applies changed characters
                if ttymode:
                    bcolorm = bcolor[cbn]
                    fcolorm = fcolor[cfn]                                               # Applies changed colors... also, the reason these 2 lines arent in an if condition in other modes is because if ttymode is False, then this script defaults to ascending mode.
                elif not ttymode:
                    bcolorm = ""
                    fcolorm = ""
            exec("num = num" + opr + "2")                                               # Controls the number of forground characters, further controlled by the operator variable opr
        elif boolrandom:
            time.sleep(random.randint(0, 1000) / 10000)                                 # Waits for a random interval between 0 and half a second
            n = random.randint(0, (len(btxt) - 1))
            cbn = random.randint(0, (len(bcolor) - 1))
            cfn = random.randint(0, (len(fcolor) - 1))
            btxtm = btxt[n]
            ftxtm = ftxt[n]
            bcolorm = bcolor[cbn]
            fcolorm = fcolor[cfn]
            if num2 == 1:                                                               # If the least number of foreground characters possible is 1, then it will make sure that the number of foreground characters generated is an odd number
                num = random.randint(num2, cols)
                if num % 2 == 0:
                    while num % 2 == 0:
                        num = random.randint(num2, cols)
            elif num2 == 2:                                                             # If the least number of foreground characters possible is 2, then it will make sure that the number of foreground characters generated is an even number
                num = random.randint(num2, cols)
                if num % 2 != 0:
                    while num % 2 != 0:
                        num = random.randint(num2, cols)
        elif booldescending:                                                            # No explanation needed... just like the first mode, but reversed...
            time.sleep(0.0625)
            if num == num2:
                opr = " + "
            elif num == cols:
                n = random.randint(0, (len(btxt) - 1))
                cbn = random.randint(0, (len(bcolor) - 1))
                cfn = random.randint(0, (len(fcolor) - 1))
                opr = " - "
                btxtm = btxt[n]
                ftxtm = ftxt[n]
                bcolorm = bcolor[cbn]
                fcolorm = fcolor[cfn]
            exec("num = num" + opr + "2")
        elif boolgay:                                                               # Its not like others... so do read...
            time.sleep(0.0625)
            n = 4                                                                   # The foreground and background character is fixed to the 5th one (ik it says 4, but indexing works differently)
            if cbn == 0 and cfn == 0:
                opr = " + "
            elif cbn == (len(bcolor) - 1) and cfn == (len(fcolor) - 1):
                opr = " - "                                                         # The same operator switch I used in the ascending block...
            exec("cbn = cbn" + opr + "1")
            exec("cfn = cfn" + opr + "1")
            btxtm = btxt[n]
            ftxtm = ftxt[n]
            bcolorm = bcolor[cbn]
            fcolorm = fcolor[cfn]
            num = cols                                                              # Locks the number of foreground characters to the width of the tty.
except KeyboardInterrupt:                                                           # Executes when Ctrl+C is pressed at anytime
    if ttymode:
        print("\033[0m")
        txt_confirm = input("Save last 1000 lines to txt? (y/n): ")                 # Already very self-explanatory. Asks the user for saving output to a txt file
        if txt_confirm == "y":
            with open("output.txt", "wt") as f:
                f.write("")
                f.close()                                                           # Creates a file output.txt with nothing written...
            with open("output.txt", "at") as f:
                if len(lins) < 1000:
                    for i in range(0, (len(lins) - 1)):
                        f.write(lins[i] + "\n")                                     # If length of lins is below 1000 it will save all of it in the txt file
                elif len(lins) >= 1000:
                    for i in range((len(lins) - 1001), (len(lins) - 1)):            # If its greater than 1000 it will save the last 1000 lines to the txt file
                        f.write(lins[i] + "\n")
                f.close()
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
