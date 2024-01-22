import subprocess
result = subprocess.run('conda env list', capture_output=True, text=True, check=True)
output = result.stdout
print(output)