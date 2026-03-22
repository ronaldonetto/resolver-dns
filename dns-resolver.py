import socket

#Function to look up the ip address of a hostname
def resolve_hostname():
   
   try:
     #Loop to display menu
     counter = 0
     while counter == 0:
         print("----------------------------------------------------------------------------")
         print("Resolve Hostname - Find out what a website's IP address is.\n")
         print("[0] Find out")
         print("[1] Exit programm\n")
      
         choice = int(input("What is your choice: "))

         if choice == 0:
           hostname = str(input("What is the website's host address: "))
           ip_address = socket.gethostbyname(hostname)
           print(f"\nHostname: {hostname}\nIP Address: {ip_address}")
         else:
           print("closing program...")
           exit()
   except ValueError: 
      print("Error: Invalid value, please enter another value")
   except socket.gaierror:
      print("Error: Address not found")
   except Exception as e:
       print(f"An unexpected error ocurred: {e}")

#Using the function
resolve_hostname()

    


