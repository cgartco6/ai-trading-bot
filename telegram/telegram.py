import telegram
from telegram.ext import Updater

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "@your_channel"

def send_telegram_alert(signal, pair, strength):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    message = f"""
    🚀 *TRADING ALERT* 🚀
    Pair: {pair}
    Signal: {signal}
    Confidence: {strength}%
    Timeframe: 5M
    Recommended: {'HIGH' if strength > 85 else 'MEDIUM'}
    """
    bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode='Markdown')

# Example usage
signal_strength = 92  # AI confidence percentage
send_telegram_alert("BUY", "USD/ZAR", signal_strength)
