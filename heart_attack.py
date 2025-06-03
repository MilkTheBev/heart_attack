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

def clearscr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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

lins = []                                                                           # Will store the lines the program prints without color...
modes = [
        "ascending",    # The first one i coded... increases the number of foreground characters until it reaches the maximum width it can, from which it begins to shrink... when it fully shrinks, a new pattern begins.
        "random",       # aka. chaos... everything is randomized after each line.... time interval, random... colors, random... characters, random...
        "descending",   # Just like the first one, but reversed... may take time....
        "gay",          # ik a bit offensive.... im sorry... it basically outputs a rainbow... each line colored differently... Oh yeah and this does not have a colorless version because it cant. So if you're sensitive to flashing lights please don't choose this....
        "file"          # A nice one, it outputs the text in a text file over and over again with colors and shit...
]

# ^^ The different modes in which it can output ^^

for i in range(0, len(modes)):
    print(str(i + 1) + ". " + modes[i])
if ttymode:
    mode = int(input("Choose mode (for example, type '1' for 'ascending' mode): ")) - 1 # Prompts the user to choose the mode... and this wont loop. So run the script again to switch mode
elif not ttymode:
    mode = 0

if mode == 4:
    file = input("Enter '.txt' file path (has to be full path, also avoid using characters like '\\', use '/' instead as backslashes are treated as escape characters, you dont need to know what an escape character is just enter the goddamn path)\n> ") # For the 5th mode (ik it says 4, but indexing works differently), a text file will need to be provided...
    with open(file, "rt") as f:
        flins = f.readlines()
    f.close()                                                                           # Does some quick line storing and then closes so that it neither bothers you or the file
    ln = 0                                                                              # ln here is not natural log, but rather the line index of the list of lines created and stored in flins
    num = 1                                                                             # Oh yeah and num is locked to 1 cuz you do not wanna see one line twice. Do you?
    t = float(input("Set time interval (in seconds, can be decimal too): "))            # For extra sexiness you choose the time interval between each line in this mode.

clearscr()

try:
    if ttymode:
        print("Press Ctrl+C to quit.\n\n")
        time.sleep(1)
    while x:
        lin = ftxtm * num                                                               # Multiplies the selected foreground character with the number...
        gap = btxtm * ((cols - len(lin)) // 2)                                          # Centers lin and fills the extra space with the background character
        gap2 = gap + (btxtm * (cols - len(gap + lin + gap)))                            # If any space still remains, fills it up with the background character
        if ftxtm == "*":
            endchar = "\r"
        else:
            endchar = "\n"
        print(bcolorm + gap + fcolorm + lin + bcolorm + gap2, end = endchar)            # Prints the output and colors as necessary
        lins.append(gap + lin + gap2)
        if mode == 0:
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
        elif mode == 1:
            time.sleep(random.randint(0, 1000) / 1000)                                  # Waits for a random interval between 0 and half a second
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
        elif mode == 2:                                                                 # Descending mode... no explanation needed... just like the first mode, but reversed...
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
                if ttymode:
                    bcolorm = bcolor[cbn]
                    fcolorm = fcolor[cfn]
                elif not ttymode:
                    bcolorm = ""
                    fcolorm = ""
            exec("num = num" + opr + "2")
        elif mode == 3:                                                                 # Gay mode... its not like others... so do read...
            time.sleep(0.0625)
            n = 4                                                                       # The foreground and background character is fixed to the 5th one as it truly resembles the pride flag (ik it says 4, but indexing works differently)
            if cbn == 0 and cfn == 0:
                opr = " + "
            elif cbn == (len(bcolor) - 1) and cfn == (len(fcolor) - 1):
                opr = " - "                                                             # The same operator switch I used in the ascending block...
            exec("cbn = cbn" + opr + "1")
            exec("cfn = cfn" + opr + "1")
            btxtm = btxt[n]
            ftxtm = ftxt[n]
            bcolorm = bcolor[cbn]
            fcolorm = fcolor[cfn]
            num = cols                                                                  # Locks the number of foreground characters to the width of the tty.
        elif mode == 4:                                                                 # File mode... this ones cool imo
            time.sleep(t)                                                               # t here is the time interval you choose at the beginning
            if ln == 0:                                                                 # If ln is 0 it changes the background colors and characters....
                n = random.randint(0, (len(btxt) - 1))
                cbn = random.randint(0, (len(bcolor) - 1))
                cfn = random.randint(0, (len(fcolor) - 1))
            btxtm = btxt[n]
            ftxtm = flins[ln].replace("\n", "")                                         # Takes the current line (ln) and replaces the '\n' escape character (newline or line feed) with nothing
            if ttymode:
                bcolorm = bcolor[cbn]
                fcolorm = fcolor[cfn]
            elif not ttymode:
                bcolorm = ""
                fcolorm = ""
            ln = ln + 1
            if ln == len(flins):
                ln = 0                                                                  # If the last line has been reached, reset back to 0
except KeyboardInterrupt:                                                               # Executes when Ctrl+C is pressed at anytime
    if ttymode:
        print("\033[0m")
        txt_confirm = input("Save last 1000 lines to txt? (y/n): ")                     # Already very self-explanatory. Asks the user for saving output to a txt file
        if txt_confirm == "y":
            with open("output.txt", "wt") as f:
                f.write("")
                f.close()                                                               # Creates a file output.txt with nothing written...
            with open("output.txt", "at") as f:
                if len(lins) < 1000:
                    for i in range(0, (len(lins) - 1)):
                        f.write(lins[i] + "\n")                                         # If length of lins is below 1000 it will save all of it in the txt file
                elif len(lins) >= 1000:
                    for i in range((len(lins) - 1001), (len(lins) - 1)):                # If its greater than 1000 it will save the last 1000 lines to the txt file
                        f.write(lins[i] + "\n")
                f.close()
        clearscr()
