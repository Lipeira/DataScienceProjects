import openai

openai.api_key = "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"

#Função gerar texto a parir do modelo de linguagem
#API para passar a mensagem para o modelo do CHATGPT 4.0

def gera_texto(texto):
    
    response = openai.Completion.create(
        
        #modelo de linguagem, outros: https://platform.openai.com/account/rate-limits
        engine = 'gpt-3.5-turbo',

        #texto inicial chatbot
        prompt = texto,

        #tamanho do texto
        max_tokens = 50,
        
        #conclusões gerar para cada promp
        n = 5,

        #não conterá sequência de parada
        stop = None,

        #medida de aleatoriedade
        #perto de 1 --> aleatorio
        #perto de 0 --> identificável
        temperature = 0.8
    )

    return response.choices[0].text.strip()    


def main():
    
    print("Bem vindo ao GPT-4 Chatbot")
    print('Digite "sair" a qualquer momento para encerrar')

    while True:
        
        #Interagir com o CHATBOT
        user_message = input("\nVocê: ")

        if user_message.lower() == "sair":
            break
      
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"

        #Invocar função -> MSG CHATBOT
        chatbot_response = gera_texto(gpt4_prompt)

        print(f"\nChatbot: {chatbot_response}")

if __name__ == "__main__":
    main()