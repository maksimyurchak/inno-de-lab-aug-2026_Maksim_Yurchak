# Collector of infrastructure metrics
import json  # for custom printing

system_telemetry = [
("srv_01", 12.5, 64, "online"),
("srv_02", 85.0, 92, "online"),
("srv_03", 0.0, 0, "offline"),
("srv_04", 45.2, 78, "online"),
("srv_05", 95.1, 99, "online")
]

# assign variables from system_telemetry and ignore servers with status: "offline"
node_name, cpu_load, ram_usage, status = [], [], [], []

for node_value, cpu_value, ram_value, status_value in system_telemetry:
    if status_value != 'offline':
        status.append(status_value)
        cpu_load.append(cpu_value)
        ram_usage.append(ram_value)
        node_name.append(node_value)

# Calculate summorized metrics
active_servers = len(node_name)
average_CPU_load = round(sum(cpu_load) / len(cpu_load), 2)
max_ram_usage = max(ram_usage)

sum_metrics = {
    'active_nodes_count': active_servers,
    'metrics': {
        'average_cpu': average_CPU_load,
        'max_ram': max_ram_usage
    }
}

print(f'Активные узлы в сети: {node_name}')
# Активные узлы в сети: ['srv_01', 'srv_02', 'srv_04', 'srv_05']
print('Итоговый отчет телеметрии:')
print(json.dumps(sum_metrics, indent=4))  # output of the print is below in """"triple double quotes""""
"""
{
    "active_nodes_count": 4,
    "metrics": {
        "average_cpu": 59.45,
        "max_ram": 99
    }
}
"""
