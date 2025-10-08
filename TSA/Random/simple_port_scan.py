VULN_PORTS = {21, 23, 445}

ports = set(map(int, input("Enter ports (comma separated): ").split(",")))
if VULN_PORTS & ports:
    print(f"Port {VULN_PORTS & ports} is potentially vulnerable.")
else: 
    print("No port is potentially vulnerable.")
