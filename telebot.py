from telegram.ext import Updater, CommandHandler
from fmkorea_crawl import fmkorea_crawl
import telegram


class TeleBotManager:
    def __init__(self, token, chat_id):
        self.bot = telegram.Bot(token)
        self.chat_id = chat_id
        self.targets = []
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.dispatcher.add_handler(CommandHandler('help', self.help))
        self.dispatcher.add_handler(CommandHandler(
            'add', self.add_target, pass_args=True))
        self.dispatcher.add_handler(CommandHandler(
            'del', self.delete_target, pass_args=True))
        self.dispatcher.add_handler(
            CommandHandler('targets', self.print_targets))

    def help(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="""
            - `/help`: 도움말
- `/add target1 target2 ...`: 타겟리스트에 타겟 추가
- `/del target1 target2 ...`: 타겟리스트에서 타겟 삭제
- `/targets`: 현재 타겟리스트 보기
            """)

    def add_target(self, update, context):
        for arg in context.args:
            if arg not in self.targets:
                self.targets.append(arg)
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f"타겟리스트에 {arg}이(가) 추가되었습니다!")
            else:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f"{arg}은(는) 이미 타겟리스트에 존재합니다!")

    def delete_target(self, update, context):
        for arg in context.args:
            if arg in self.targets:
                self.targets.remove(arg)
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f"{arg}이(가) 타겟리스트에서 삭제되었습니다!")
            else:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f"{arg}은(는) 타겟리스트에 존재하지 않습니다!")

    def print_targets(self, update, context):
        if not self.targets:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="타겟리스트가 비었습니다.")
            return

        result = "노리고 있는 타겟리스트"
        for target in self.targets:
            result += "\n" + "-" + target
        context.bot.send_message(chat_id=update.effective_chat.id, text=result)

    def crawl(self):
        result = fmkorea_crawl(self.targets)
        if result:
            for item in result:
                self.bot.send_message(self.chat_id, text=item)

    def start_bot(self):
        self.updater.start_polling()
