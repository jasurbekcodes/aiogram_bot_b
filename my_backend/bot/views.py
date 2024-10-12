from django.http import JsonResponse
from aiogram import Bot, Dispatcher
from aiogram.types import Update
import asyncio

bot = Bot(token="8125936730:AAFtw79qXQT8dQiFGruDamFlYt_LzyO2Duw")

dp = Dispatcher()


async def handle_update(request):
    update = Update.de_json(request.body.decode('utf-8'))
    await dp.start_polling(update)
    return JsonResponse({'status': 'ok'})
