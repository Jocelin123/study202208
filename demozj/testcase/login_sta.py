import os,sys
#os.path.dirname获取项目根目录,导入一个模块时默认情况下搜索当前目录、已安装的内置模块和第三方模块，如果搜索不到就会报错，把搜索路径存放在sys模块中的path中
#即添加到了系统的环境变量路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

