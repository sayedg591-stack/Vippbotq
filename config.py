"""
Configuration settings for the Quotex VIP Channel Bot
"""

import os  

class Config:
    # Bot configuration
    BOT_TOKEN = os.getenv('BOT_TOKEN', '8164851203:AAFk7NK11SkXOR8rPVIWWfCxBOpyzjAxEuQ')
    
    # Telegram API configuration for user account verification
    TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID', '26649092')
    TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH', '798c30bdd5f430a78dea56dc8a09b1b3')
    TELEGRAM_PHONE_NUMBER = os.getenv('TELEGRAM_PHONE_NUMBER', '+916392645473')
    
    # Admin configuration
    ADMIN_USER_IDS = [int(x.strip()) for x in os.getenv('ADMIN_USER_IDS', '').split(',') if x.strip()]
    
    # Database configuration
    DATABASE_PATH = 'quotex_bot.db'
    
    # Bot messages
    WELCOME_MESSAGE = """
    👋 Hello, Trader 🤍

    📥 Please enter your Quotex Trader ID (numbers only) 🔢.

    🔍 We’ll verify your details, and within 1 minute ⏱️, you’ll receive the exclusive BILLIONAIRE VIP channel link 🔗.

    🤝 Thank you for your patience and cooperation! 🙏✨ Your journey to success starts here 🚀💼.

     📞 For Support: @BILLIONAIREBOSS101 💬"""
    
    HELP_MESSAGE = """
📋 Available Commands:

🔹 /start - Start the bot and see welcome message
🔹 /verify <quotex_user_id> - Verify your Quotex registration
🔹 /help - Show this help message

📝 **How to get VIP access:**

1️⃣ Register on Quotex using our link:
https://broker-qx.pro/sign-up/?lid=996329

2️⃣ Find your User ID in your account settings

3️⃣ Use: /verify [your_user_id]

Example: /verify 12345678

🛠️ Admin Commands:
🔹 /admin_add_links - Add VIP channel links
🔹 /admin_stats - Show bot statistics
🔹 /admin_users - List verified users
    """
    
    VERIFICATION_SUCCESS = "🎉 Verification successful! Welcome to our VIP community! Here's your exclusive VIP channel link:"
    VERIFICATION_FAILED = """Hello Trader,

It appears that your account is not registered using my link. ❌

Create your Quotex account with this secure link:

🔗 https://broker-qx.pro/sign-up/?lid=996329

Note: If you already have an account before but not linked with me then delete the existing id and create new with the link above to get entry in the YASHODA VIP Channel"""
    ALREADY_VERIFIED = "✅ You're already a verified VIP member! Check your previous messages for your VIP link."
    NO_LINKS_AVAILABLE = "❌ VIP links are temporarily unavailable. Our team has been notified and will resolve this shortly."
    INVALID_USER_ID = """❌ Please provide a valid Quotex User ID.

📝 Format: /verify [your_user_id]
📋 Example: /verify 12345678

💡 Find your User ID in your Quotex account settings."""
    
    # Verification timeout (seconds)
    VERIFICATION_TIMEOUT = 30
