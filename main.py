from telebot import TeleBotManager
from dotenv import load_dotenv
from scheduler import SchedulerManager
import os

if __name__ == '__main__':
    load_dotenv()

    TOKEN = os.getenv("TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    telebot_manager = TeleBotManager(token=TOKEN, chat_id=CHAT_ID)
    telebot_manager.start_bot()

    scheduler_manager = SchedulerManager()
    scheduler_manager.add_schedule(
        telebot_manager.crawl, 10)  # interval = seconds
    scheduler_manager.start_scheduler()
