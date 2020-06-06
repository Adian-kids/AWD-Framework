import SSH_Config
def Show_Server_List(Site_Nums):                                             #展示服务器列表
	Server_list = open("SSH_Config.txt","r")
	next(Server_list)
	for i in range(Site_Nums):
		Config_list = eval(Server_list.readline()[11:])                      #处理字符串，读取为字典
		print( "Server[%d]  ==> "%i + "IP : " + Config_list[0] + "   Username : "+ Config_list[2] + "   Password : " + Config_list[3])




def Get_Single_Shell(Site_Nums):                                             #进入单个Linux交互环境
	Show_Server_List(Site_Nums)
	Server_Number = input("Input Which Server you want  : ") 
	if int(Server_Number) > Site_Nums:
		print("Wrong Choice")
		Get_Single_Shell(Site_Nums)
	SSH_Config.UseShell(Server_Number)


def Send_to_All(Site_Nums):                                                  #向所有服务器发送指令
	Command = input("Command:")
	for i in range(Site_Nums):
		SSH_Config.Send_Command(i)


def Download_Code_Data(Site_Nums):                                           #下载所有的源码和数据文件
	pass
def Upload_files(Site_Nums):                                                 #上传文件
	pass
def Download_log(Site_Nums):                                                 #下载日志
	pass