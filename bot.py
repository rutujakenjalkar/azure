from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext

# Bot Adapter
settings = BotFrameworkAdapterSettings(app_id="", app_password="")
adapter = BotFrameworkAdapter(settings)

async def messages_handler(request):
    body = await request.json()
    activity = body.get("text", "Hello!")
    
    async def send_reply(turn_context: TurnContext):
        await turn_context.send_activity(f"You said: {activity}")

    await adapter.process_activity(body, "", send_reply)
    return web.Response(text="Bot message received", status=200)

# Create Web Server
app = web.Application()
app.router.add_post("/api/messages", messages_handler)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=3978)
