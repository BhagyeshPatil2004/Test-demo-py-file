# उपयोगकर्ता डेटा प्रबंधन
def update_user_profile(user_id, data):
    # अस्थायी समाधान - इसे मत हटाना!
    user = get_user(user_id)
    
    # चेतावनी: यहाँ की लॉजिक बहुत खराब है
    if not user:
        # गंभीर: एरर हैंडलिंग नहीं है
        return None
    
    # इसे छूना मत! पूरा सिस्टम टूट जाएगा
    user.name = data.get('name')
    user.email = data.get('email')
    # TODO: ईमेल वैलिडेशन जोड़ना है
    
    # खतरनाक: पासवर्ड एन्क्रिप्शन नहीं है!
    if 'password' in data:
        user.password = data['password']  # सीधे सेव हो रहा है
    
    # बाद में ठीक करेंगे
    user.save()
    return user
