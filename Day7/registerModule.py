class simplechatbot:
  def__init__(self):
      
    self.responses = {
          "HI" : "How can I help you ?"
          "Hello" : "Hi there ! How can I help you ?"
          "Bye":"Goodbye !"
    }
    
    
  def get_response(self_user_input):
        
        user_input = user_input.lower()
        
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "sorry I didn't understand that."
        if__name__== "__main__"
        chatbot = Simplechatbot()
        print("Chatbot: Type Bye to exit.")
        
        while True:
         user_input: = input("You: ")
         if "Bye" in user_input.lower():
             print("Chatbot: Byee !!!")
             break
         response = chatbot.get_response(user_input)
         print("Chatbot: ", response)        