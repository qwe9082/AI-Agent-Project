# 🔢 数论与表示函数
# 1.ceil(x)：向上取整，返回不小于 x 的最小整数。
# 2.floor(x)：向下取整，返回不大于 x 的最大整数。
# 3.fabs(x)：返回 x 的绝对值（浮点数）。
# 4.factorial(x)：返回正整数 x 的阶乘。
# fmod(x, y)：取模运算，结果符号与 x 相同，适合浮点数。
# frexp(x)：返回 (尾数, 指数) 元组，使 x = 尾数 * 2**指数。
# ldexp(x, i)：返回 x * (2**i)，是 frexp 的反函数。
# modf(x)：返回 (小数部分, 整数部分) 元组，均为浮点数。
# trunc(x)：截断小数部分，返回整数部分。
# copysign(x, y)：返回 x 的绝对值加上 y 的符号。
# fsum(iterable)：精确浮点求和，比内置 sum 精度更高。
# gcd(a, b)：返回 a 和 b 的最大公约数。
# lcm(a, b)：返回 a 和 b 的最小公倍数（Python 3.9+）。
# comb(n, k)：组合数 C(n, k)（Python 3.8+）。
# perm(n, k)：排列数 P(n, k)（Python 3.8+）。
# isqrt(n)：整数平方根，返回不大于 √n 的最大整数（Python 3.8+）。
# prod(iterable)：返回可迭代对象所有元素的乘积（Python 3.8+）。
# remainder(x, y)：IEEE 754 风格的余数（Python 3.7+）。
# isclose(a, b)：判断两个值是否接近（可设相对/绝对容差）。
# isfinite(x)：判断是否为有限数（非无穷大/非 NaN）。
# isinf(x)：判断是否为正/负无穷大。
# isnan(x)：判断是否为 NaN（非数字）。
# 📈 幂函数与对数函数
# exp(x)：返回 e 的 x 次幂。
# expm1(x)：返回 e 的 x 次幂减 1，小数值时精度更高。
# log(x[, base])：自然对数，可指定底数。
# log1p(x)：返回 log(1+x)，接近 0 时精度更高。
# log2(x)：以 2 为底的对数。
# log10(x)：以 10 为底的对数。
# pow(x, y)：返回 x 的 y 次幂（浮点数）。
# sqrt(x)：返回 x 的平方根。
# cbrt(x)：返回 x 的立方根（Python 3.11+）。
# 📐 三角函数与角度转换
# sin(x)、cos(x)、tan(x)：三角正弦、余弦、正切，x 为弧度。
# asin(x)、acos(x)、atan(x)：反正弦、反余弦、反正切，返回弧度。
# atan2(y, x)：返回坐标点 (x, y) 的方位角（弧度）。
# hypot(*coords)：欧几里得范数，即 sqrt(sum(x**2))，支持多维。
# dist(p, q)：两点之间的欧几里得距离（Python 3.8+）。
# degrees(x)：弧度转角度。
# radians(x)：角度转弧度。
# 🔄 双曲函数
# sinh(x)、cosh(x)、tanh(x)：双曲正弦、余弦、正切。
# asinh(x)、acosh(x)、atanh(x)：反双曲正弦、余弦、正切。
# ⚙️ 特殊函数
# erf(x)：误差函数。
# erfc(x)：互补误差函数。
# gamma(x)：伽马函数（阶乘在实数域的推广）。
# lgamma(x)：伽马函数绝对值的自然对数。
# 📦 数学常量
# math.pi：圆周率 π ≈ 3.14159。
# math.e：自然常数 e ≈ 2.71828。
# math.tau：τ = 2π ≈ 6.28318。
# math.inf：正无穷大。
# math.nan：非数字（NaN）。
# math.phi：黄金比例 ≈ 1.61803（Python 3.8+）。
