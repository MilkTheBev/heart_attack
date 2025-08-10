###############################################################################################
#                                                                                             #
#                                                                                             #
#                                                                                             #
#   ███      ███   ████████████      ██████      █████████      ████████████                  #
#   ███      ███   ███            ███      ███   ███      ███       ████                      #
#   ████████████   ████████████   ████████████   ████████████       ████                      #
#   ███      ███   ███            ███      ███   ███    ███         ████                      #
#   ███      ███   ████████████   ███      ███   ███     ████       ████                      #
#                                                                                             #
#                                                                                             #
#                                                                                             #
#      ██████      ████████████   ████████████      ██████         █████████   ███     ████   #
#   ███      ███       ████           ████       ███      ███   ███            ███    ███     #
#   ████████████       ████           ████       ████████████   ███            █████████      #
#   ███      ███       ████           ████       ███      ███   ███            ███    ███     #
#   ███      ███       ████           ████       ███      ███      █████████   ███     ████   #
#   (as it is actually called...)                                                             #
#                                                                                             #
#   A nice little tty screensaver made in python                                              #
#                                                                                             #
###############################################################################################
import os, time, random, argparse

def clearscr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

x = True                                                                            # Will be used for looping
opr = " + "
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
        "gay",          # ik a bit offensive.... im sorry... it basically outputs a rainbow... each line colored differently...
        "file",         # A nice one, it outputs the text in a text file over and over again with colors and shit...
        "zigzag"        # Unique as the number of foreground characters dont change, the center of those foreground characters does.
]

parser = argparse.ArgumentParser(description="heart_attack.py")                     # Added argument parsing.. LESGOOOOOOOO!!!! say goodbye to having to input the mode all the time.
parser.add_argument("mode", choices = ["0", "1", "2", "3", "4", "5", "6"], help = "0 - Non-tty (for environments that are not tty's, ttymode becomes False), 1 - ascending, 2 - random, 3 - descending, 4 - gay, 5 - file, 6 - zigzag") # The mode argument set up...
parser.add_argument("--file", type = str, help = "The file required for 'file' mode.") # An optional argument required for file mode, which is the text file its gonna read and make colorful.
args = parser.parse_args()                                                          # Tells argparse to parse the arguments and realize they exist, which you don't.

mode = int(args.mode) - 1
if mode == -1:
    ttymode = False
    mode = 0
else:
    ttymode = True

if ttymode:
    cols = os.get_terminal_size().columns                                           # Finds the number of columns
else:
    cols = 80                                                                       # If not a tty, 80 is assumed to be the number of columns
if cols % 2 == 0:
    num2 = 2                                                                        # If the number of columns is an even number, then the minimum number of foreground characters is 2
elif cols % 2 != 0:
    num2 = 1                                                                        # Similarly, if the number of columns is an odd number, then the minimum number of foreground characters is 1.
num = num2                                                                          # num here is the current number of foreground characters. num2 remains constant while num changes (except mode 6).
t = 5 / cols                                                                        # Divides 5 by cols to get the time it should sleep for...

if mode == 4 and args.file:
    with open(args.file, "rt") as f:
        flins = f.readlines()
    f.close()                                                                       # Does some quick line storing and then closes so that it neither bothers you or the file
    ln = 0                                                                          # ln here is not natural log, but rather the line index of the list of lines created and stored in flins
    num = 1                                                                         # Oh yeah and num is locked to 1 cuz you do not wanna see one line twice. Do you?
    t = float(input("Set time interval (in seconds, can be decimal too): "))        # For extra sexiness you choose the time interval between each line in this mode, ik you still have to input time but am i here to keep on making arguments? No.
elif mode == 4 and not args.file:
    print("Uhh... im clueless rn so like can you run the script again and make sure to use the '--file' argument if choosing 'file' mode?")
    exit()

if mode == 5:
    rem = 0                                                                         # rem here is the count for gap, or the multiplier for gap...

if ttymode:
    clearscr()

try:
    if ttymode:
        print("Press Ctrl+C to quit.\n\n")
        time.sleep(1)
    while x:
        lin = ftxtm * num                                                           # Multiplies the selected foreground character with the number...
        if mode != 5:
            gap = btxtm * ((cols - len(lin)) // 2)                                  # Centers lin and fills the extra space with the background character IF the mode isnt zigzag
        elif mode == 5:
            gap = btxtm * rem                                                       # Now what if it was zigzag, you may ask, well this... Here the gap is what we HAVE to change, not what GETS changed by the mode. Now how will we change it? Read and find out...
        gap2 = btxtm * (cols - len(gap + lin))                                      # If any space still remains, fills it up with the background character
        if ftxtm == "*":
            endchar = "\r"
        else:
            endchar = "\n"
        print(bcolorm + gap + fcolorm + lin + bcolorm + gap2, end = endchar)        # Prints the output and colors as necessary
        lins.append(gap + lin + gap2)
        if mode == 0:
            time.sleep(t)                                                           # Waits t seconds
            if num == cols:
                opr = " - "                                                         # If the number of foreground characters is the same as the number of columns, operation becomes subtraction
            elif num == num2:
                n = random.randint(0, (len(btxt) - 1))                              # Changes the foreground and background characters
                cbn = random.randint(0, (len(bcolor) - 1))                          # Changes background character color
                cfn = random.randint(0, (len(fcolor) - 1))                          # Changes foreground character color
                opr = " + "                                                         # Changes operation to addition if the number of foreground characters are the lowest that they can be...
                btxtm = btxt[n]
                ftxtm = ftxt[n]                                                     # Applies changed characters
                if ttymode:
                    bcolorm = bcolor[cbn]
                    fcolorm = fcolor[cfn]                                           # Applies changed colors... also, the reason these 2 lines arent in an if condition in other modes is because if ttymode is False, then this script defaults to ascending mode.
                elif not ttymode:
                    bcolorm = ""
                    fcolorm = ""
            exec("num = num" + opr + "2")                                           # Controls the number of forground characters, further controlled by the operator variable opr
        elif mode == 1:
            time.sleep(random.randint(0, 1000) / 10000)                             # Waits for a random interval between 0 and half a second
            n = random.randint(0, (len(btxt) - 1))
            cbn = random.randint(0, (len(bcolor) - 1))
            cfn = random.randint(0, (len(fcolor) - 1))
            btxtm = btxt[n]
            ftxtm = ftxt[n]
            bcolorm = bcolor[cbn]
            fcolorm = fcolor[cfn]
            if num2 == 1:                                                           # If the least number of foreground characters possible is 1, then it will make sure that the number of foreground characters generated is an odd number
                num = random.randint(num2, cols)
                if num % 2 == 0:
                    while num % 2 == 0:
                        num = random.randint(num2, cols)
            elif num2 == 2:                                                         # If the least number of foreground characters possible is 2, then it will make sure that the number of foreground characters generated is an even number
                num = random.randint(num2, cols)
                if num % 2 != 0:
                    while num % 2 != 0:
                        num = random.randint(num2, cols)
        elif mode == 2:                                                             # Descending mode... no explanation needed... just like the first mode, but reversed...
            time.sleep(t)
            if num == num2:
                opr = " + "
            elif num == cols:
                n = random.randint(0, (len(btxt) - 1))
                cbn = random.randint(0, (len(bcolor) - 1))
                cfn = random.randint(0, (len(fcolor) - 1))
                opr = " - "
                btxtm = ftxt[n]
                ftxtm = btxt[n]
                bcolorm = fcolor[cbn]
                fcolorm = bcolor[cfn]
            exec("num = num" + opr + "2")
        elif mode == 3:                                                             # Gay mode... its not like others... so do read...
            time.sleep(t)
            n = 4                                                                   # The foreground and background character is fixed to the 5th one as it truly resembles the pride flag (ik it says 4, but indexing works differently)
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
        elif mode == 4:                                                             # File mode... this ones cool imo
            time.sleep(t)                                                           # t here is the time interval you choose at the beginning
            if ln == 0:                                                             # If ln is 0 it changes the background colors and characters....
                n = random.randint(0, (len(btxt) - 1))
                cbn = random.randint(0, (len(bcolor) - 1))
                cfn = random.randint(0, (len(fcolor) - 1))
            btxtm = btxt[n]
            ftxtm = flins[ln].replace("\n", "")                                     # Takes the current line (ln) and replaces the '\n' escape character (newline or line feed) with nothing
            bcolorm = bcolor[cbn]
            fcolorm = fcolor[cfn]
            ln = ln + 1
            if ln == len(flins):
                ln = 0                                                              # If the last line has been reached, reset back to 0
        elif mode == 5:                                                             # Zigzag mode, the hardest mode i have ever worked on...
            time.sleep(t)
            num = cols // 4                                                         # This doesnt change, unlike in other modes. Its constant... Also this is how we will change gap.
            if rem == 0:
                n = random.randint(0, (len(btxt) - 1))
                cbn = random.randint(0, (len(bcolor) - 1))
                cfn = random.randint(0, (len(fcolor) - 1))
                opr = " + "
                btxtm = btxt[n]
                ftxtm = ftxt[n]
                bcolorm = bcolor[cbn]
                fcolorm = fcolor[cfn]
            elif rem == cols - num:
                n = random.randint(0, (len(btxt) - 1))
                cbn = random.randint(0, (len(bcolor) - 1))
                cfn = random.randint(0, (len(fcolor) - 1))
                opr = " - "
                btxtm = btxt[n]
                ftxtm = ftxt[n]
                bcolorm = bcolor[cbn]
                fcolorm = fcolor[cfn]
            exec("rem = rem" + opr + "1")                                           # Basically used the addition with operator toggling logic type shit in this mode, just changed the afftected variable. Its now rem instead of num as like i *rem*'d before (pun intended), num stays constant.
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
        clearscr()
