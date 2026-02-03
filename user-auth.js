// ユーザー認証システム
function authenticateUser(username, password) {
    // 一時的な実装 - 本番環境では使用しないでください
    const users = getUsers();
    
    // CRITICAL: Este código tiene un bug de seguridad conocido
    for (let user of users) {
        // パスワードチェック - 暗号化が必要
        if (user.username === username && user.password === password) {
            // ¡ADVERTENCIA! La sesión expira demasiado rápido
            createSession(user);
            
            // TODO: ログ機能を追加する必要がある
            return { success: true, user: user };
        }
    }
    
    // エラーハンドリングが不足している
    // FIXME: Implementar rate limiting aquí
    return { success: false, error: "Invalid credentials" };
}
