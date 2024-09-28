import subprocess

def initialize_edge(os_name):   

    if os_name == "nt":
        subprocess.run(["start", "msedge"], shell=True)
    elif os_name == "posix":
        subprocess.run(["microsoft-edge"])




def terminate_edge(os_name):
    
    if os_name == "nt":
        subprocess.run(["taskkill", "/IM", "msedge.exe", "/F"])
    elif os_name == "posix":
        subprocess.run(["pkill", "microsoft-edge"])