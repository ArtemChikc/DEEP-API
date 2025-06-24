from openai import OpenAI



class dpsk:
    def __init__(self, api_key, messages_limit=7, prompt="You are a helpful assistant"):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.messages_limit = messages_limit
        self.del_history(prompt)

    def chat(self, text, think=False, stream=False):
        self.messages.append({"role": "user", "content": text})

        response = self.client.chat.completions.create(
            model="deepseek-chat" if not think else "deepseek-reasoner",
            messages=self.messages,
            stream=stream)
        self.messages.append({
            "role": response.choices[0].message.role,
            "content": response.choices[0].message.content
        })

        while len(self.messages)>=self.messages_limit:
            for i, msg in enumerate(self.messages):
                if i>0 and msg["role"]!="system":
                    del self.messages[i]
                    break

        return response.choices[0].message.content

    def del_history(self, prompt="You are a helpful assistant"):
        if prompt:
            self.prompt = prompt
        self.messages = [{"role": "system", "content": self.prompt}]



if __name__=="__main__":
    ai = dpsk("your api key")
    while True:
        print(f"DeepSeek: {ai.chat(input("User: "))}\n")
