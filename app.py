from flask import Flask, redirect, url_for, render_template

languages_questions = [("Which programming language is commonly used for web development and is known for its flexibility and simplicity?", "JavaScript"),
                      ("What is the primary purpose of using loops in programming?", "To iterate over a block of code multiple times until a certain condition is met."),
                      ("Identify the programming language developed by Sun Microsystems in the mid-1990s, often used for building enterprise-level applications.", "Java"),
                      ("What are the key differences between statically typed and dynamically typed programming languages?", "Statically typed languages require variable types to be explicitly declared at compile time, whereas dynamically typed languages infer variable types at runtime."),
                      ("Explain the difference between pass by value and pass by reference in the context of function parameter passing.", "Pass by value creates a copy of the actual parameter's value, while pass by reference passes the memory address of the actual parameter.")]

frameworks_questions = [("This popular JavaScript framework is commonly used for building single-page web applications.", "Angular"),
                      ("Identify the framework used for building scalable and maintainable web applications, known for its Model-View-Controller architecture.", "Ruby on Rails"),
                      ("What is the purpose of dependency injection in software development, and which popular framework implements this concept extensively?", "Dependency injection is used to achieve inversion of control by injecting dependencies into a component rather than the component creating them. Angular extensively implements dependency injection."),
                      ("Explain the concept of middleware in the context of software frameworks, and provide an example of a framework that heavily utilizes middleware.", "Middleware is software that acts as a bridge between an operating system or database and applications, often used for request processing. Express.js is a framework that heavily utilizes middleware in Node.js applications."),
                      ("Discuss the differences between Django and Flask, two popular web frameworks in Python, in terms of their architecture, scalability, and flexibility.", "Django is a high-level framework that follows the 'batteries-included' approach, providing a full-featured ORM, admin panel, and authentication system out of the box. Flask, on the other hand, is a microframework that offers more flexibility and allows developers to choose their own components, making it more lightweight and scalable for smaller projects.")]

hardware_questions = [("What is the primary function of a CPU in a computer?", "Processing data and executing instructions."),
                      ("This component of a computer stores data temporarily for quick access by the CPU.", "RAM"),
                      ("What does RAM stand for, in the context of computer hardware?", "RAM stands for Random Access Memory."),
                      ("Identify this component in a computer which manages data transfer between the CPU, memory, and other peripherals.", "Northbridge or Memory Controller"),
                      ("What is the purpose of a GPU in a computer, and how does it differ from a CPU?", "GPU (Graphics Processing Unit) is specialized in rendering graphics and performs parallel tasks more efficiently than a CPU, which focuses on sequential processing and general-purpose computing.")]

OOP_questions =     [("What is the main idea behind encapsulation in object-oriented programming?", "Encapsulation is the bundling of data and methods that operate on that data into a single unit, also known as a class."),
                      ("Explain the concept of inheritance in object-oriented programming, and provide an example.", "Inheritance allows a class (subclass) to inherit properties and methods from another class (superclass). Example: A 'Car' class can inherit from a 'Vehicle' class, inheriting properties like 'speed' and methods like 'start_engine()'."),
                      ("Identify the four main principles of object-oriented programming, often abbreviated as 'SOLID'.", "SOLID stands for Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle."),
                      ("Discuss the concept of polymorphism in object-oriented programming, and how it can be achieved in different programming languages.", "Polymorphism allows objects to be treated as instances of their parent class, enabling code to work with objects of multiple types. It can be achieved through method overriding (dynamic polymorphism) or method overloading (static polymorphism)."),
                      ("Explain the difference between composition and inheritance in object-oriented design, and discuss scenarios where each approach is preferred.", "Inheritance involves creating new classes by extending existing ones, while composition involves constructing classes using instances of other classes. Composition is preferred when there is a has-a relationship between objects, promoting code reusability and flexibility. Inheritance is suitable when there is an is-a relationship between objects, promoting code organization and conceptual clarity.")]

mystery_questions = [("What connects two elements of a linked list?", "A node"),
                    ("What is the method that returns the top of a stack?", "pop()"),
                    ("Explain the difference between a stack and queue", "A stack is FILO, a queue is FIFO"),
                    ("Why can't a queue be instantiated", "Because it is an interface-a description of how something that is a queue should behave"),
                    ("Explain the difference between a HashMap and a HashTable","A HashTable is synchronized to prevent multiple threads from accessing it at once; a HashMap isn't")]

@app.route("/")
def board():
    return render_template("board.html")            

@app.route("/question/<category>/<val>")
def question(category=None, val=0):
    is_clicked = False
    if category == "h":
        cat = hardware_questions
    elif category == "l":
        cat = languages_questions
    elif category == "f":
        cat = frameworks_questions
    elif category == "o":
        cat = OOP_questions
    else:
        cat = mystery_questions
    return render_template("question.html", question = cat[int(val)-1][0], answer = cat[int(val)-1][1])

if __name__ == "__main__":
    app.run(debug=True)