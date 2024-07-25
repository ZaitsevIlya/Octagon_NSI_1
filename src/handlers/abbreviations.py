from g4f.client import Client
from g4f.Provider import HuggingChat
 
client = Client(
    provider = HuggingChat
)
 
def answer(question: str) -> str: 
    response = client.chat.completions.create( 
        model="command-r+", 
        messages=[{"role": "user", "content": "Преобразуй сокращения присутствующие в сообщении в полные слова. Это название должности в мужском роде, могут присутсвовать слова среднего рода. Учитывай все сокращения, не пропускай никакие. Не добавляй слов, которых не было в исходном сообщении. Может встречаться частица НЕ. В ответе предоставь сообщение без сокращений и без пропусков букв. Вот это сообщение: " + question}], 
    ) 
    return response.choices[0].message.content 
 
def main(): 
    question = "Вр.не исп.об.зам.дир.отд.прод."
    print(answer(question)) 