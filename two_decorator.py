        
def decorator1(greet):
        def pattern1():
               print("*****")
               greet()
               print("*****")
        return pattern1
        
def decorator2(greet):
        def pattern2():
               print("%%%%%")
               greet()
               print("%%%%%")
        return pattern2
    
@decorator1
       
@decorator2
def greet():
         print("Hello")
        
greet()
