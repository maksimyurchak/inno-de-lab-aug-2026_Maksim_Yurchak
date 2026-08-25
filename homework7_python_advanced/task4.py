# Module of audit security 
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# Delete duplicates in requested_roles
requested_roles = set(requested_roles)

# Find common roles
common_roles = requested_roles & required_admin_roles

# Find missing roles which weren't requested by users
missing_roles = required_admin_roles - requested_roles

# Check if 'security_officer' role in requested_roles with high-speed method O(1)
is_security_officer = 'security_officer' in requested_roles

print(f'Уникальные запрошенные роли: {requested_roles}')  # {'admin', 'guest', 'developer'}
print(f'Общие административные роли: {common_roles}')  # {'admin'}
print(f'Недостающие административные роли: {missing_roles}')  # {'audit_manager', 'security_officer'}
print(f'Наличие роли security_officer в запросе: {is_security_officer}')  # False
