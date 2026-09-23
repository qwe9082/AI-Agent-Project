# 📁 文件和目录操作
# 1.获取与切换目录‌：os.getcwd() 返回当前工作目录；os.chdir(path) 切换工作目录。
# 2.列出目录内容‌：os.listdir(path='.') 返回指定目录下所有文件和子目录的列表。
# 3.创建目录‌：os.mkdir(path) 创建单级目录（父目录必须存在）；os.makedirs(path) 递归创建多级目录，配合 exist_ok=True 可避免已存在时报错。
# 4.删除目录‌：os.rmdir(path) 删除空目录；os.removedirs(path) 递归删除空目录（遇到非空即停）。
# 5.删除文件‌：os.remove(path) 直接删除文件，不走回收站。
# 6.重命名/移动‌：os.rename(src, dst) 重命名文件或目录；os.replace(src, dst) 功能类似，但目标已存在时会直接覆盖。
# 7.遍历目录树‌：os.walk(path) 生成器，递归返回 (当前路径, 子目录列表, 文件列表)，适合批量处理文件。
# 8.获取文件信息‌：os.stat(path) 返回文件状态（大小、修改时间、权限等）。
# 🔗 路径处理（os.path）
# 这部分是 os 的子模块，专门处理路径字符串，不实际访问磁盘。
#
# 1.拼接与拆分‌：os.path.join(a, b) 拼接路径；os.path.split(path) 拆成 (目录, 文件名) 元组；os.path.splitext(path) 拆成 (主名, 扩展名)。
# 2.获取组成部分‌：os.path.dirname(path) 返回目录部分；os.path.basename(path) 返回文件名部分。
# 3.路径判断‌：os.path.exists(path) 是否存在；os.path.isfile(path) 是否为文件；os.path.isdir(path) 是否为目录；os.path.isabs(path) 是否为绝对路径。
# 4.路径转换‌：os.path.abspath(path) 转绝对路径；os.path.realpath(path) 解析符号链接返回真实路径；os.path.normpath(path) 规范化路径（去掉 .. 和冗余斜杠）。
# 5.文件信息‌：os.path.getsize(path) 文件字节大小；os.path.getmtime(path) 最后修改时间；os.path.getatime(path) 最后访问时间。
# ⚙️ 系统与环境
# 1.环境变量‌：os.environ 字典，可直接读写环境变量（如 os.environ.get('HOME')）；os.getenv(key, default=None) 获取单个变量。
# 2.执行命令‌：os.system(command) 在 shell 中执行命令，返回退出码。⚠️ 它拿不到命令输出，需要捕获输出时用 subprocess 模块更合适。
# 3.平台信息‌：os.name 返回平台标识（Windows 是 'nt'，Linux/Mac 是 'posix'）；os.sep 路径分隔符（Windows \，Linux /）；os.linesep 换行符。
# 4.进程信息‌：os.getpid() 当前进程 ID；os.getppid() 父进程 ID；os.getcwd() 工作目录。
# 🧠 进程管理（偏 Unix）
# 这部分主要在 Linux/Mac 上可用，Windows 支持有限。
# 1.用户与权限‌：os.getuid() 真实用户 ID；os.geteuid() 有效用户 ID；os.getgid() 组 ID。
# 2.进程组‌：os.getpgrp() 当前进程组 ID；os.getpgid(pid) 指定进程的组 ID。
# 3.调度优先级‌：os.getpriority(which, who) 获取进程/进程组/用户的调度优先级。