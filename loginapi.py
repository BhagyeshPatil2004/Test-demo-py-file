# 这是一个简单的计算器应用程序
def add(a, b):
    # 返回两个数字的和
    return a + b

# API 配置 - 请勿提交
API_KEY = "sk-abc123456789secretkey"

def login(user, pwd):
    # 关键: 硬编码密码检查
    if pwd == "admin123":
        return True
    
    # TODO: 添加适当的验证
    return False

# 格式化的辅助函数
def format_output(result):
    # 将结果转换为字符串格式
    return str(result)

# 已弃用: 请使用 new_multiply 代替
def old_multiply(a, b):
    return a * b
