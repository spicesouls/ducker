#!/bin/env python3
from src.templates import *
from src.messaging import *

from colorama import init, Style, Fore, Back
init()
import argparse
import sys


banner = Fore.YELLOW + Style.BRIGHT + fr"""
 ____  _  _   ___  __ _  ____  ____    __
(    \/ )( \ / __)(  / )(  __)(  _ \ <(o )___
 ) D () \/ (( (__  )  (  ) _)  )   /  ( ._^ /
(____/\____/ \___)(__\_)(____)(__\_)   `---'{Fore.RESET}
┌────────────────────────────────────────────
└─ {Fore.YELLOW}spicesouls.github.io/ducker
""" + Style.RESET_ALL

print(banner)

# Args

parser = argparse.ArgumentParser(description='Generate rubber ducky payloads with ease.')

parser.add_argument('--payload', type=str, help='A File Containing Your Payload.')
parser.add_argument('-m', choices=['cmd', 'powershell', 'notepad'], help='Mode: Where to inject your payload.')
parser.add_argument('-d', type=int, default=1000, help='The Delay you want between executing lines of your payload in milliseconds. (1000 By Default)')
parser.add_argument('-o', type=str, help='The file to save the finalised script to, the finalised script is outputted in the terminal by default.')

args = parser.parse_args()


if not args.payload:
    alert('Please supply a Payload.')
    sys.exit()

if not args.m:
    alert('Please select a Mode.')
    sys.exit()

if not args.o:
    clioutput = True
    output = 'None'
else:
    clioutput = False
    output = args.o

#########################
### SCRIPT GENERATION ###
#########################
info('Payload: ' + args.payload)
info('Mode: ' + args.m)
info('Delay: ' + str(args.d))
info('Output: ' + output)
print('')

info('Generating Ducky Payload...')
try:
    if args.m == 'cmd':
        script = cmd(args.payload, str(args.d))
    elif args.m == 'powershell':
        script = powershell(args.payload, str(args.d))
    elif args.m == 'notepad':
        script = notepad(args.payload, str(args.d))
except FileNotFoundError:
    warn('Error: Payload File Supplied is not found. Exiting...')
    sys.exit()

good('Finished!')

if clioutput == True:
    info('Showing Finalised Script...')
    print('\n--- SCRIPT START ---')
    for i in script:
        print(i)
    print('--- SCRIPT END ---\n')
else:
    info('Saving Finalised Script To: ' + output)
    with open(output, 'w') as o:
        for i in script:
            o.write(i + '\n')
        o.close()
    good('Finalised Script Saved To: ' + output)
