from pwn import *
# Set up the binary with QEMU for AArch64
binary = './prospectors_claim'
context.binary = binary
context.arch = 'aarch64'  # Specify the correct architecture

# Try to solve it symbolically first
payload = "PCTF/{24d16126d6739d6ada82b125534d2ae2324b39ed72e5a1200c5ac96200/}"

# Start the process with QEMU for AArch64, specify the path to AArch64 libraries
p = process(['qemu-aarch64', '-L', '/usr/aarch64-linux-gnu', binary])

# Send the solution or run interactively
if payload:
    p.sendline(payload.encode())
else:
    print("Using interactive mode since solver failed")
    
p.interactive()