import random
responses = {
      'hello': 'Hello! how are you',
      'hi': 'Hi! how is your day'
}

def chatbot ():
        while True:
            my_input = input("You: ").lower()
            if my_input == "stop":
                print("Chatbot: goobye :(")
                break
                
            response = responses.get (my_input, "Sorry i cannot understand")
             
            print(f'Chatbot: {response}')
      
chatbot()