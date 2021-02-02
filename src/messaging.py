from colorama import init, Fore, Back, Style
init()

def good(message):
    print(f'[ {Fore.GREEN}*{Fore.RESET} ] ' + str(message))
'''
[ * ] asdf
'''

def info(message):
    print(f'[ {Fore.YELLOW}?{Fore.RESET} ] ' + str(message))
'''
[ ? ] asdf
'''

def warn(message):
    print(f'[ {Fore.RED}!{Fore.RESET} ] ' + str(message))
'''
[ ! ] asdf
'''

def alert(message):
    print('###' + '#' * len(str(message)) + '###\n## ' + Fore.RED + Style.BRIGHT + str(message) + Style.RESET_ALL + ' ##\n###' + '#' * len(str(message)) + '###')
    
'''
##########
## asdf ##
##########
'''
