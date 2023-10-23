import socket

target = input("Enter the IP address to scan: ")
options = input("do you want to have customs (c), common ports (o) or all ports (a) scanned? ")
options = options.lower()
if options == "c":
    ports = [int(x) for x in input("Enter the ports you want to scan, separated by a space: ").split()]
    print(f"scanning ports {ports}")
elif options == "o":
    ports = [20,21,22,23,25,53,67,68,69,80,110,119,123,137,138,139,143,161,162,389,443,445,465,514,587,636,993,995,1433,1521,1723,3306,3389,5432,5900,8080,10000]
elif options == "a":
    ports = [x for x in range(1,65536)]
else:
    print("invalid option, using common ports")
    ports = [20,21,22,23,25,53,67,68,69,80,110,119,123,137,138,139,143,161,162,389,443,445,465,514,587,636,993,995,1433,1521,1723,3306,3389,5432,5900,8080,10000]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")

    sock.close()