# Programme for analyzing database configuration
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# extract host and port values
print(db_config["connection"].get("host", "default_host"), '- host value')
print(db_config["connection"].get("port", "default_port"), '- port value')
print()  # for better readability 

# Check 'ssl_settings' key, if not exist, add it and a default value
db_config['ssl_settings'] = db_config.get("ssl_settings", "verify-full")

# Change user name into 'admin'
db_config["connection"]["user"] = 'admin'

# Add new key in connection with specified value
db_config["connection"]['max_connections'] = 100

# Output updated configuration in "connection"
print(f'SSL Mode: {db_config['ssl_settings']}')
print('Параметры соединения:')
for key, value in db_config["connection"].items():
    print(f'* {key}: {value}')
