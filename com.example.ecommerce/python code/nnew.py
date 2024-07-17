# print('''dgcyuegcyg
#       ccygeyucyuehcuyih
#       fcjuecybecbefbncune''')
# import pyttsx3
# engine = pyttsx3.init()

# engine.say("Hello My Name is Udit Aggarwal")
# engine.runAndWait()
import pyttsx3
import sys

# text =input("Enter Any Texthw")
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    engine.setProperty('rate', 125)
    say = '''Hello everyone! I am Udit and this is my team including Saurabh,Sachin,Pankaj,Sahil and Rohil .
Today, I'm excited to walk you through our E-Commerce application built using Spring Boot and JPA. This application supports a range of functionalities essential for running a successful e-commerce platform.
Our application provides comprehensive features including managing customers, products, orders, carts, reviews, and wishlists, ensuring a complete shopping experience.
We've utilized modern technologies such as Spring Boot for rapid development, Spring Data JPA and Hibernate for data persistence, and MySQL as our database. J son is used for data interchange.
The Prerequisites of our project are Java 11 or higher, Maven for project management, and MySQL for the database setup.
First, clone the repository from GitHub and navigate into the project directory.
Next, create a MySQL database and update the application.properties file with your database credentials.
To build and run the application, use Maven commands to clean, install dependencies, and run the Spring Boot application.
Our application exposes various RESTful API endpoints for different functionalities. Let's go through each category.
The customer endpoints allow you to create, read, update, and delete customer records.
Similarly, the product endpoints provide CRUD operations for managing products.
Order endpoints let you manage customer orders, including creation, retrieval, updating, and deletion.
The cart endpoints handle adding items to the cart, viewing the cart by customer ID, and removing items from the cart.
Review endpoints allow customers to leave reviews for products and view reviews based on product ID.
Wishlist endpoints support adding products to a wishlist, viewing the wishlist by customer ID, and removing items from the wishlist.
Here are example J son payloads for each entity to help you understand the data format required by our API endpoints.
This is an example of a customer J son payload. It includes fields like first name, last name, mobile number, email, password, created date, and card number.
Here we have a product J son payload example. It includes the product name, price, description, manufacturer, quantity, category, status, and seller information.
This is an example of a review J son payload, including review content, rating, product ID, and customer ID.
Lastly, here is a wishlist J son payload example, showing the customer ID and product ID.
If you encounter issues, make sure your database is running and correctly configured. Detailed error messages can be found in the logs.
We welcome contributions! If you find any issues or want to add new features, feel free to submit a pull request or open an issue on GitHub.
Thank you for your attention. I'm now open to any questions you might have about the project.
'''
    # say = input("Enter text here")
    engine.say(say)
    engine.runAndWait()

if __name__ == "__main__":
    text = sys.argv[0]
    speak(text)
