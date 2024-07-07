def update_server_config(file_path,key,value):
  #Read theexisting configuration of sever.conf file
	with open(file_path,'r') as file:
	 	lines=file.readlines()

 #update theconfiguration value for a specific key
	with open(file_path,'w') as file:
	 	for line in lines:
			#check if the line starts with specified key
			if key in line:
				#update the file with new value
				file.write(key + "=" + value + "\n")
			else:
				#keep the same value
				file.write(line)


#path to server configuration file 
server_config_file='server.conf'

#key and new value for which server.conf files need to be updated
key_to_update='MAX_CONNECTIONS'
new_value='1000'   #new maximum connections allowed


#update the server.conf file
update_server_config(server_config_file,key_to_update,new_value)

