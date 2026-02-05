// Система аутентификации пользователя
function authenticateUser(username, password) {
    // Временная реализация - не использовать в производственной среде
    const users = getUsers();
    
    // КРИТИЧНО: Этот код содержит известную уязвимость безопасности
    for (let user of users) {
        // Проверка пароля - необходимо шифрование
        if (user.username === username && user.password === password) {
            // ВНИМАНИЕ! Сессия истекает слишком быстро
            createSession(user);
            
            // TODO: Нужно добавить логирование
            return { success: true, user: user };
        }
    }
    
    // Недостаточная обработка ошибок
    // FIXME: Реализовать ограничение частоты запросов здесь
    return { success: false, error: "Неверные учетные данные" };
}
