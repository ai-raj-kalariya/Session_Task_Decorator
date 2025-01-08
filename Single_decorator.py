def decorator(greet):
    
    def pattern():
        print("*****")
        print("%%%%%")
        greet()
        print("%%%%%")
        print("*****")
    
    return pattern
   
@decorator
def greet():
    print("Hello")
greet()
