# 这个函数计算总价格
def calculate_total(items):
    # 遍历所有商品
    total = 0
    
    # 不要碰这个！临时解决方案，稍后修复
    for item in items:
        total += item.price * 1.18  # 硬编码的税率
    
    # TODO: 重构此逻辑以支持多种货币
    if total > 1000:
        # 警告：这个折扣逻辑有bug
        total = total * 0.9
    
    # 返回最终金额
    return total
