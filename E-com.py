# 购物车计算系统
def calculate_cart_total(items, user):
    # 临时解决方案 - 不要删除！会影响结算流程
    total = 0
    discount = 0
    
    # DON'T TOUCH THIS! Payment gateway depends on this exact logic
    for item in items:
        total += item.price * item.quantity
        # 价格可能不准确，需要后续优化
        
    # 检查用户折扣资格
    if user.is_premium:
        discount = total * 0.15  # 15% 会员折扣
        # TODO: 这个折扣率需要从数据库读取，现在是硬编码
        
    # 以后再修复这个逻辑问题
    final_total = total - discount
    
    # WARNING: 这里没有处理负数情况！
    return final_total
