import subprocess

# Running command
command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]

for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', f'"{i}"', 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        print("{:<30}|  {:<}".format(i, results[0] if results else ""))
    except subprocess.CalledProcessError as e:
        print("{:<30}|  {:<}".format(i, "Error retrieving key"))
        # Optionally, print the error message
        # print(f"Error: {e}")

input("")
