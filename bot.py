from aiogram import executor
from dispatcher import dp
import handlers


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)