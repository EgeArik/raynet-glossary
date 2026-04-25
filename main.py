# Developer  : Ege ARIK


# Raynet Junior Tech Glossary 

tech_dictionary = { 

"Python": "A high-level programming language.", 
"Git": "A distributed version control system.",
"Firewall":"Network analyze and protection device. ",
"Docker":"Gives a oppurtionaty to work in isolated workspaces.",
"Subnet":"A subnet is a smaller part of a larger network used to organize traffic and improve security.",
"Git": "A distributed version control system." ,
"Class": "A blueprint used to create objects in programming.",
"API": "A set of rules that allows different software to communicate with each other. ",
"Bug": "An error or flaw in a program that causes incorrect behavior.",
"Algorithm" : "A step by step process to solve a problem.",
"Loop" : "Runs the same code again and again. it has become uncontrollable"
} 

def list_terms(): 
    for term, desc in tech_dictionary.items(): 
        print(f"{term}: {desc}") 

list_terms() 





