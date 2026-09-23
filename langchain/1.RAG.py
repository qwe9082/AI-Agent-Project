# RAG 检索增强生成，为大模型提供了：从特定数据源检索到的信息，以此来修正和补充生成的答案
# 总结为一个公式：RAG = 检索技术 + LLM提示
# 提示RAG标准流程 1.索引 2.检索 3.生成

# 向量：把一段文本的语义信息，转换成一串固定长度的数字列表、
# 向量维度: 可以更精准的完成语义匹配, text-embedding-v1模型可以生成1536维的向量
# 余弦相似度：抛开长度的影响，得到方向的夹角，计算公式：两个向量的点积 / 两个向量的模长的乘积
import numpy as np
vec_a = [0.5, 0.5]
vec_b = [0.7, 0.7]
vec_c = [0.7, 0.5]
vec_d = [-0.6, -0.5]

# 计算点积
def sum_dot(vec_a, vec_b):
    sum_square = 0
    for a, b in zip(vec_a, vec_b):
        sum_square += a * b
    return sum_square

# 计算向量模长
def sum_mo(vec):
    sum_square = 0
    for v in vec:
        sum_square += v * v
    return np.sqrt(sum_square)

# 计算余弦相似度 两个向量的点积 / 两个向量的模长的乘积
def sum_yu(vec_a, vec_b):
    return sum_dot(vec_a,vec_b) / (sum_mo(vec_a)*sum_mo(vec_b))

print(f"ab {sum_yu(vec_a, vec_b)}")
print(f"ac {sum_yu(vec_a, vec_c)}")
print(f"ad {sum_yu(vec_a, vec_d)}")