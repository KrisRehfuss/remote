import subprocess

ip_to_site = {
    "10.47.8.142": "Crum Lynn",
    "10.47.8.206": "411 Sutton Ave",
    "10.47.8.186": "Aston warehouse",
    "10.47.2.210": "Aston warehouse",
    "10.47.8.134": "CFH Springfield",
    "10.47.30.4": "CFH Springfield",
    "10.47.234.3": "CMA",
    "10.47.4.2": "Lamerch",
    "10.47.5.5": "Mac dade",
    "10.47.5.1": "Mac dade",
    "10.47.8.7": "Media Imaging",
    "10.47.33.25": "Media Imaging",
    "10.47.33.18": "Media Imaging",
    "10.47.33.1": "Media Imaging",
    "10.47.8.230": "Milton park",
    "10.47.8.170": "Sharon Hill",
    "10.47.8.226": "Haverford 403",
    "10.47.8.190": "Han Brinton Lake",
    "10.47.3.176": "Han Brinton Lake",
    "10.47.3.166": "Han Brinton Lake",
}

def ping_ip(ip):
    try:
        # For Windows
        output = subprocess.check_output(
            ["ping", "-n", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True
        )
        if "Received = 1" in output:
            return True
    except subprocess.CalledProcessError:
        pass

    try:
        # For UNIX-like systems
        output = subprocess.check_output(
            ["ping", "-c", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True
        )
        if "1 packets received" in output:
            return True
    except subprocess.CalledProcessError:
        pass

    return False

def main():
    unresponsive_ips = []

    for ip, site in ip_to_site.items():
        result = ping_ip(ip)
        if result:
            print(f"{ip} ({site}) is UP")
        else:
            print(f"{ip} ({site}) is DOWN")
            unresponsive_ips.append(ip)

    if unresponsive_ips:
        print("\nThe following IP addresses did not respond:")
        for ip in unresponsive_ips:
            print(f"{ip} ({ip_to_site[ip]})")
    else:
        print("All IP addresses responded successfully.")

if __name__ == "__main__":
    main()
