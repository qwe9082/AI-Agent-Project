# 🎲 基础随机数
# 1.random.random()：生成 [0.0, 1.0) 区间内的随机浮点数，是模块的基础函数。
# 2.random.uniform(a, b)：生成 [a, b] 范围内的随机浮点数，a 和 b 的顺序无关紧要。
# 3.random.randint(a, b)：生成 [a, b] 闭区间内的随机整数（包含两端）。
# 4.random.randrange(start, stop[, step])：从 range(start, stop, step) 中随机选一个整数，左闭右开，支持步长。
# 5.random.getrandbits(k)：生成 k 个随机比特位的非负整数，适合指定位数的随机整数。‌
# 🔀 序列操作
# 1.random.choice(seq)：从非空序列中随机返回一个元素。
# 2.random.choices(population, weights=None, *, cum_weights=None, k=1)：有放回地抽取 k 个元素，支持权重或累积权重。
# 3.random.sample(population, k, *, counts=None)：无放回地抽取 k 个唯一元素，不修改原序列；counts 可指定重复元素数量（Python 3.9+）。
# 4.random.shuffle(x)：原地打乱列表顺序，返回 None，直接修改原列表。‌
# 📊 概率分布
# 1.random.triangular(low, high, mode)：三角分布。
# 2.random.betavariate(alpha, beta)：Beta 分布。
# 3.random.expovariate(lambd=1.0)：指数分布，lambd 为平均值的倒数。
# 4.random.gammavariate(alpha, beta)：Gamma 分布。
# 5.random.gauss(mu=0.0, sigma=1.0)：正态分布（高斯分布），速度稍快。
# 6.random.lognormvariate(mu, sigma)：对数正态分布。
# 7.random.normalvariate(mu=0.0, sigma=1.0)：正态分布，线程安全版本。
# 8.random.vonmisesvariate(mu, kappa)：冯·米塞斯分布（角度分布）。
# 9.random.paretovariate(alpha)：帕累托分布。
# 10.random.weibullvariate(alpha, beta)：威布尔分布。‌
# 🛠️ 状态与系统
# 1.random.seed(a=None, version=2)：初始化随机数生成器；相同种子可复现随机序列，a 可为 None、整数、字符串等。
# 2.random.getstate()：返回生成器当前内部状态，可与 setstate() 配合恢复。
# 3.random.setstate(state)：恢复到之前 getstate() 时的状态。
# 4.random.randbytes(n)：生成 n 个随机字节（Python 3.9+）。
# 5.random.SystemRandom：基于 os.urandom() 的类，提供系统级随机源，序列不可重现，不依赖软件状态。‌
