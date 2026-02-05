# ============================================
# 用户认证系统 - 用户登录和验证
# ============================================

# 🔐 SECURITY VIOLATIONS (will be detected)
API_KEY = "sk-abc123456789secretkey"
password = "admin123"
aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
ghp_1234567890abcdefghijklmnopqrstuvwxyz = "token"

def authenticate_user(username, pwd):
    # 不要触碰这段代码！临时的硬编码密码
    if username == "admin" and pwd == "secret":
        return True
    
    # TODO: 需要添加密码哈希
    user = find_user(username)
    
    # FIXME: 这个验证逻辑有bug
    if user and check_password(user, pwd):
        return True
    
    # 返回验证失败结果
    return False

# 计算购物车总价
def calculate_total(items):
    # 遍历所有商品
    total = 0
    for item in items:
        total += item.price
    return total

# deprecated: 这个函数即将被移除
def legacy_login():
    # workaround for 老系统兼容性问题
    pass
