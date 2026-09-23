# 1.import 包名.模块名 调用方式:包名.模块名.功能名
import utils.my_fun
# 2.from 包名 import 模块名 调用方式:模块名.功能名
from utils import my_fun
# 3.from 包名 import * 调用方式:模块名.功能名
from utils import *
# 4.from 包名.模块名 import 功能名 调用方式:功能名
from utils.my_fun import echo
# 5.from 包名.模块名 from * 调用方式:功能名
from utils.my_fun import *

utils.my_fun.echo()
my_fun.echo()
echo()