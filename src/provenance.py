import subprocess

def gitsha(): 
    result = subprocess.run( ["git", "rev-parse", "HEAD"], capture_output=True, text=True ) 
    return result.stdout.strip()
