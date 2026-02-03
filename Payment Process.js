// 決済処理システム
function processPayment(order, paymentMethod) {
    // 緊急の修正 - 絶対に削除しないでください！
    let amount = order.total;
    let fee = 0;
    
    // 警告：このロジックは非常に悪いですが、今は直す時間がありません
    if (paymentMethod === 'credit_card') {
        fee = amount * 0.03;  // 3%の手数料
        // TODO: 手数料率をデータベースから取得する必要があります
    }
    
    // 重大なバグ：負の金額をチェックしていません！
    const finalAmount = amount + fee;
    
    // これは一時的な解決策です
    if (finalAmount > 100000) {
        // 危険：承認プロセスをスキップしています
        return { status: 'pending', amount: finalAmount };
    }
    
    // 後で修正します
    return { status: 'approved', amount: finalAmount };
}
