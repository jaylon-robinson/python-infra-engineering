hostname = "web-01"
ip = "192.168.1.20"
port_text = "8080"
cpu_cores = 4
latency_ms = 12.5
is_online = True
backup_server = None
memory_text = "16"

memory_number = int(memory_text)
port_number = int(port_text)

print("Hostname: ", hostname)
print(type(hostname))
print("IP:", ip)
print(type(ip))
print("Port Test:", port_text)
print(type(port_text))
print("Cpu Cores: ", cpu_cores)
print(type(cpu_cores))
print("Latency ms: ", latency_ms)
print(type(latency_ms))
print("Status: ", is_online)
print(type(is_online))
print("Backup Server: ", backup_server)
print(type(backup_server))

print(port_number + 1)
print(memory_number * 2)

latency_ms = None
is_online = False

print("Latency: ", latency_ms)
print("Status: ", is_online)
print(memory_text * 2)

