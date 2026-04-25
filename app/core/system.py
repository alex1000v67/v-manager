import subprocess

def uptime():
    uptime = subprocess.run("uptime", shell=True, capture_output=True, text=True)
    return {"output": uptime.stdout.strip()}

def get_free_ozu():
    ozu = subprocess.run("free -m | awk 'NR==2{print $4}'", shell=True, capture_output=True, text=True)
    return ozu.stdout.strip()