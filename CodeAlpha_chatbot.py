def chatbot(input):
    input = input.lower().strip()
    if input in ["hello","hello!","hi!","hi","hey","hii"]:
        return "Hi! Nice to meet you "
    elif input in ["how are you","how r you", "how are u", "how are you?"]:
        return "I'm doing great! Thanks for asking."
    elif input in ["good morning"]:
        return "Good morning."
    elif input in ["good evening"]:
        return "Good evening."
    elif input in ["good afternoon"]:
         return "Good afternoon."
    elif input in["i am doing good","i am doing great","i am doing well","i am doing nice"]:
         return "Great.Thats a good thing I hear from you."
    elif input in ["what is your name","what is your name?", "who are you","who are you?"]:
        return "I'm a rule-based chatbot created using Python."
    elif input in ["thank you","thankyou","thanks"]:
        return "You are welcome."
    elif input in ["what is python"]:
        return "Python is a high-level, interpreted, and easy-to-learn programming language."
    elif input in ["what is programming"]:
        return "Programming is the process of writing instructions for a computer to perform tasks."
    elif input in["what can you do","what can you do for me","what can you do for me?","what can you do?","help","how can you help","how can you help?","how can you help me","how can you help me?","commands"]:
        return "I can chat with you.I can give replays to some questions."
    elif input in ["bye", "goodbye","good bye", "exit","quit","see you","ok then","see you soon","see you later"]:
        return "Goodbye! Have a great day"
    else:
        return "Sorry, I didn't understand that. Can you try something else?"

def run():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        userinput = input("You: ")
        response = chatbot(userinput)
        print("Chatbot:", response)
        if userinput.lower() in ["bye", "goodbye","good bye", "exit","quit","see you","ok then","see you soon","see you later"]:
            break
        elif "bye" in userinput:
            break

run()
