
I want to create a chat app that allows a user to write to an AI assistant. So it will always be a one way connection.
The chat app should be developed using fasthtml and htmx for web framework. Pydantic-ai for AI assistant and a crud framework for saving data to disk.
The chat app will be part of a larger application handling authentication etc.. So everything besides the chat app is handled.

The chat should be establishing a websocket connection. When a websocket connection is established then a UserSession should be created. The user session has an active ipython shell, chat message history etc..
The user session should just be kept in memory in a python dictionary. Each user should at most be able to have one active session.
The session should handle the chat life cycle with restoring shell namespace if previous conversation and handling messages etc.. And also cleanup when disconnecting.

The websocket connection should stream html. The html streamed should represent pydantic-ai nodes. So each html returned is pydantic-ai node in an agent.iter loop

The html should be an append only structure. With the caveat that a user might go back and edit a message which should delete all messages after the edited message and then continue the append only structure.

Note all the AGENTS.md included contain specific knowledge about the project structure.

See the pydantic_ai.md file in the project for docs on pydantic-ai

I have create some initial code, which can be considered pseudocode'ish,
### User flow

```python
from pathlib import Path
from fasthtml.common import Script, RedirectResponse, Beforeware
from ui.core import daisy_app
from app.routes.chat import ar as chat_routes
from varro.db import crud, models

DEMO_USER_ID = 1

def before(req, sess):
	user = crud.user.get(DEMO_USER_ID)
	# Attach scoped instances to request
	req.scope["user"] = user
	req.scope["chats"] = crud.chat.for_user(user.id)


beforeware = Beforeware(before, skip=STATIC_SKIP)
# Create FastHTML app with DaisyUI + Plotly + Alpine.js
app, rt = daisy_app(exts='ws')
# Configure and mount chat routes
chat_routes.to_app(app)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=5001)
```

### Websockets

```python
@app.ws('/ws')
async def on_message(msg:str, send, chat_id):

	# Send user message back immediately
	await send(Div(
		UserMessage(message),
		hx_swap_oob="beforeend",
		id="message-area"
	))
	
	# Clear input
	await send(ChatInput())
	
	# Stream AI response
	async for block in agent_html_stream(msg, ):
		await send(Div(
			block,
			hx_swap_oob="beforeend",
			id="assistant-stream"
	
	))	
```


### Chat session

See varro/chat/session.py

### Routes

```python
@ar("/chat/history")
def chat_history(chats: CrudChat):
    return ChatDropdown(chats.get_recent(limit=10))

@ar("/chat/delete/{chat_id}")
def chat_delete(sess, user: User, chats: CrudChat, chat_id: int):
    chat = chats.get(chat_id)
    if not chat:
        return Response(status_code=404)
    chats.delete(chat)
    # ...
    
@ar("/chat/create/{user_id}")
def chat_create(sess, user_id):
	chat = models.Chat(user_id=user_id)
	chat = chats.create(chat)
	sess["chat_id"] = chat.id
	...

```


