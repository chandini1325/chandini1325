def college_chatbot():
    print("Welcome to AU College Chatbot!")
    print("How can I help you today?")
    print("You can ask about: Admissions, Courses, Fees, Contact, Location or type 'bye' to leave.")

    while True:
        user_input = input("You: ").lower()

        if "admission" in user_input:
            print("Chatbot: Admissions are open from September. Visit our website for the application form.")
        elif "course" in user_input:
            print("Chatbot: We offer courses in Engineering, Business,Law, Arts, and Science.")
        elif "fee" in user_input or "fees" in user_input:
            print("Chatbot: The annual fees range from $60,000 to $65,000 depending on the course.")
        elif "contact" in user_input:
            print("Chatbot: You can contact us at 1234567890 or email info@AUcollege.edu.")
        elif "location" in user_input:
            print("Chatbot: We are located at Visakhapatnam.")
        elif "bye" in user_input:
            print("Chatbot: Thank you for visiting AU College. Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Please ask something else.")

# Run the chatbot
college_chatbot()
