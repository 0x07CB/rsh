from sh import sh
from sh import ErrorReturnCode
from sh import Command as Cmd
from sh import ifconfig
from sh import hping3
from multiprocessing import Process
import socket ,requests
command_=""

# class to create an static http server
class StaticServer:
    def __init__(self, port=80, path='.', host='0.0.0.0'):
        self.port = port
        self.path = path
        self.host = host
        self.server = None
        self.process = None
    # function to set the port
    def set_port(self, port):
        self.port = port
        return self
    # function to set the path
    def set_path(self, path):
        self.path = path
        return self
    # function to set the host
    def set_host(self, host):
        self.host = host
        return self
    # function to start the server
    def start(self,print_url=True):
        self.process = Process(target=self._start)
        self.process.start()
        if print_url:
            self.show_url()
        return self
    # function to stop the server
    def stop(self):
        self.process.terminate()
        return self
    # function to start the server
    def _start(self):
        self.server = Cmd('python3 -m http.server {} -d {}'.format(self.port, self.path))
        self.server(_bg=True)
        return self
    # function to get the url
    def get_url(self):
        return 'http://{}:{}'.format(self.host, self.port)
    # function named 'show_url' to display the url returned by 'self.get_url()'
    def show_url(self):
        print("The URL is: {}".format(self.get_url()))
        return self


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
