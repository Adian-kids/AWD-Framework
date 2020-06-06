def SSH_Config_Input(Site_Nums):
	Config_Path = "SSH_Config.txt"
	Save_SSH = open(Config_Path,"w")
	for i in range(Site_Nums):   #SSH 信息
		SSH_Config = {}
		SSH_Config[0] = input("Server %d IP:===>"%i)
		SSH_Config[1] = input("Server %d Port:==>"%i)
		SSH_Config[2] = input("Server %d Pass:==>"%i)
		Save_SSH.write("Server %d : "%i +str(SSH_Config) + "\n")
	print("All The Config Saved in SSH_Config.txt Successful")
	Save_SSH.close()
