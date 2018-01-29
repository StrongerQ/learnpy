'''

select caption from permission left join permission_to_role on ...
where role_id = %s


left join
inner join

'''

permission_list = [
    {'caption': '添加用户', 'func': 'add', 'module': 'user_info'},
    {'caption': '删除用户', 'func': 'delete', 'module': 'user_info'},
    {'caption': '查看用户', 'func': 'fetch', 'module': 'user_info'}
]
for index, item in enumerate(permission_list, 1):
    print(index, item['caption'])

# 1
# 添加用户
# 2
# 删除用户
# 3
# 查看用户

choice = input('请输入要选择的菜单？')
choice = int(choice)
permission = permission_list[choice - 1]
func_name = permission['func']

####### 根据字符串动态导入模块
import importlib #根据字符串动态导入模块的模块
#执行文件导入模块后,之后的其他py文件就不用再导入了
name = 'src.user_info'
func = 'add'
m = importlib.import_module(name)
fun = getattr(m,func) #反射,返回函数
func()