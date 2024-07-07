def update_server_config(file_path, key, value):
    # Read the existing configuration of the server.conf file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update the configuration value for a specific key
    with open(file_path, 'w') as file:
        for line in lines:
            # Check if the line starts with the specified key
            if line.startswith(key + "="):
                # Update the line with the new value
                file.write(key + "=" + value + "\n")
            else:
                # Keep the same value
                file.write(line)

# Path to server configuration file
server_config_file = 'server.conf'

# Key and new value for which the server.conf file needs to be updated
key_to_update = 'MAX_CONNECTIONS'
new_value = '1000'  # New maximum connections allowed

# Update the server.conf file
update_server_config(server_config_file, key_to_update, new_value)
