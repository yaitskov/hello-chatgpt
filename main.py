from  openai import AsyncOpenAI
import tornado.ioloop
import tornado.web
import os

client = AsyncOpenAI(api_key=os.getenv('MY_OPENAI_KEY'))

class MainHandler(tornado.web.RequestHandler):
    #@gen.coroutine
    async def get(self):
        theQ = self.get_argument("q", default="noquestion")
        if theQ == "noquestion":
            self.write("No question is provided. Pass the question in q parameter.")
        else:
            print(f"Request: {theQ}")
            resp = await client.chat.completions.create(
                messages = [
                    {
                        "role": "user",
                        "content": theQ,
                    }
                ],
                model="gpt-3.5-turbo"
            )
            respMsg = resp.choices[0].message.content
            print(f"Response: {respMsg}")
            self.write(f"""<div><h3>Ответ:</h3><pre style="word-wrap:break-word; white-space:pre-wrap;">{respMsg}</pre></div>""")

def make_app():
    return tornado.web.Application([
        (r"/answer", MainHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "static", "default_filename": "index.html"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server listening on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
