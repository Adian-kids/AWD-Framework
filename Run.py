import sys
sys.path.append(r'Files/')
import Print_text  #/Files/Print_text.py
import SSH_Config  #/File/SSH_Config.py
import paramiko    #SSH相关库

Print_text.Print_Welcome_Message() #输出欢迎信息
if __name__ == '__main__':   
	print("Start!!!!!!!!!!")
	Site_Nums = int(input("Number of sites:")) 
	Web_Dir = ["/var/www/html/*", "/home/wwwroot/*", "/app/*", "/usr/local/nginx/html/*"] #Web目录列表
	SSH_Config.SSH_Config_Input(Site_Nums)

		
	Print_text.Usage() #输出Usage

