#This script updates a key-value pair in a configuration file.
def update_server_config(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith(key + "="):
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

server_config_file = 'server.conf'
key_to_update = 'MAX_CONNECTIONS'
new_value = '1000'
update_server_config(server_config_file, key_to_update, new_value)
##############################explaination#################################
#Explanation:

#Reads the configuration file and stores its lines.
#Rewrites the file, updating the line with the specified key.