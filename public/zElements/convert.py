import os

# 获取当前目录下的所有文件和文件夹
for root, dirs, files in os.walk("."):
    for name in files + dirs:
        if " " in name:
            # 构造当前文件或文件夹的完整路径
            old_path = os.path.join(root, name)
            # 替换文件名中的空格为下划线
            new_name = name.replace(" ", "_")
            # 构造新的完整路径
            new_path = os.path.join(root, new_name)
            # 重命名文件或文件夹
            os.rename(old_path, new_path)
            print(f'Renamed: {old_path} -> {new_path}')

print("所有文件和文件夹已重命名完成。")
