import ollama

client = ollama.Client(host="http://localhost:11434")

class ModelConnector:
    def __init__(self, model_name: str = "qwen3:4b"):
        self.model_name = model_name

    def chat(self, user_prompt: str) -> str:
        response = client.chat(
            model=self.model_name,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
        return response["message"]["content"]

if __name__=="__main__":
    model = ModelConnector()
    print(model.chat("hello"))