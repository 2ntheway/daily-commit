import os
import datetime

# 仓库路径
repo_path = "/path/to/your/repo"
os.chdir(repo_path)

# 更新内容
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("log.txt", "a") as file:
    file.write(f"Commit on {today}\n")

# Git 操作
os.system("git add .")
os.system(f"git commit -m 'Auto commit on {today}'")
os.system("git push origin main")
