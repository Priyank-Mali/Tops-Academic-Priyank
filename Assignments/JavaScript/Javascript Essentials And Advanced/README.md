![image](https://www.datocms-assets.com/48401/1628644950-javascript.png?auto=format&fit=max&w=1200)

## 1] JavaScript Introduction

* **What is JavaScript? Explain the role of JavaScript in web development.**
    >Javascript is high-level interpreted programmig language for createing dynamic pages.

    > for interactive & dynamic web pages without reloading pages(ex: cricket live score)

    > for external source we can fetch API using JS. 

* **How is JavaScript different from other programming languages like Python or Java?**
    > JavaScript runs on browser and also on server via Node.js

    > it is dynamically type like python

    > DOM manipulation through different events 

* **Discuss the use of `<script>` tag in HTML. How can you link an external JavaScript file to an HTML document?**
    > `script` tag is used for writing js code 

    > create `script.js` file and link to `html.index` through `<script link="script.js"></script>` before ending of `</body>` tag:

## 2] Variables and Data Types

* __What are variables in JavaScript? How do you declare a variable using var, let, and const?__
    > variables is like container to store data at memory and retrive that data through name of that variable;

    > 🌈 `var name = "priyank"`

    > 🌈 `let number = 10 `

    > 🌈 `const pi = 3.14 `

* __Explain the different data types in JavaScript. Provide examples for each.__
    > there are many datatype in JS

    * premitive (immutable)
        * Number
        * undefined
        * String
        * Symbol
        * Boolean
        * null

    * non-premitive (mutable)
        * object
        * function

* **What is the difference between undefined and null in JavaScript?**
    > Undefined : means it is declare but not assign any value
            
            """
                let n;
                console.log(n);  // undefined
            """
    > null : basically `typeof(null)` is `object`
         represent the absence of any object

## 3] JavaScript Operators

* **What are the different types of operators in JavaScript? Explain with examples.**
    * Arithmetic operators
    > `+ - / % * ** // ` 
    * Assignment operators
    > `= += -= /= */ %=`
    * Comparison operators
    > `== === != `
    * Logical operators
    > `&& || ^ `


* **What is the difference between `==` and `===` in JavaScript?**
    > `==` is to compare two value

    > `===` is to compare value as well as data type (for strickly check we use `===`)

## 4] Control Flow (If-Else, Switch)

* __What is control flow in JavaScript? Explain how if-else statements work with an example__
    > is we want to run code based on the condition we use `if-else` keywords

        """
            let age = 10

            if(age>18){
                console.log("you can drive")
            } else {
                console.log("can't dive")
            }
            
        """

* __Describe how switch statements work in JavaScript. When should you use a switch statement instead of if-else?__
    > when we have multiple condition to check then use `switch`

        """
            let day = 1

            switch(day){
                case 1:
                    console.log("This is Monday")
                    break
                case 2:
                    console.log("This is Tuesday")
                    break
                case 3:
                    console.log("This is Wednesday")
                    break
                case 4:
                    console.log("This is Thrusday")
                    break
                case 5:
                    console.log("This is Friday")
                    break
                case 6:
                    console.log("This is Saturday")
                    break
                case 7:
                    console.log("This is Sunday")
                    break  
            }
        """

## 5] Loops (For, While, Do-While)

* __Explain the different types of loops in JavaScript `(for, while, do-while)`. Provide a basic example of each.__
    

    > ## for
    >     """
    >        let num = 10
    >
    >        for (let i=1;i<=10;i++){
    >           console.log(`${num} * ${i} ==> ${num*i}`)
    >         }
    >     """

    > ## while
    >     """
    >        let num = 10;
    >        let i = 1;
    >
    >        while (i<=10){
    >           console.log(`${num} * ${i} ==> ${num*i}`)
    >         }
    >     """

    > ## do while
    >     code execute atleast one time even if condition of while is not satisfied
    >
    >     """
    >        let num = 10;
    >        let i = 1;
    >        do{
    >           console.log("code executed atelest one time")
    >        } while (i<0)
    >

* __What is the difference between a while loop and a do-while loop?__
    > in `do-while loop` : the `do` block of code executes even if condition of `while` loop is wrong

    > in `while loop` : first check the condition then code should be executed 

## 6] Functions

* __What are functions in JavaScript? Explain the syntax for declaring and calling a function__
    > function means block of code to perform a specif task.
        
           function <function_name( )>{        
                    block of code
            }

           <function_name( )

* __What is the difference between a function declaration and a function expression?__
         
         it support hoistning
         hello();

         function hello(){   
             return  "hello world";    
        }        
        ------------------------------------
        hello();      // Cannot access 'hello' before initializatio

        const hello = function(){
            console.log("hello world");
        }

    

* **Discuss the concept of parameters and return values in functions.**

        parameter is for dynamic usability

        function add(a,b){
            return a+b
        }
        add(10,9)

        this will return 19 value for my input
        based on the different (input) parameter it gives me different return value

## 7] Arrays

* __What is an array in JavaScript? How do you declare and initialize an array?__
    > array is JS data structure that allows to store multiple values in a single variable.

    > `let fruits = ["apple", "banana","cherry"]`

    > `let numbers = new Array(1,2,3,4)` 

* __Explain the methods `push()`, `pop()`, `shift()`, and `unshift()` used in arrays.__
    > `push()` : add element at the end
    
    > `pop()` : delete from the end
    
    > `shift()` : delete from start
    
    > `unshift()` : add element at the beigining



## 8] Objects    

* __What is an object in JavaScript? How are objects different from arrays?__
    > object is an entity which have state and behaviour (basically `key-value` pair)

        > Objects
        access via keys
        represent real-world entities

        > array
        access via indexing (ordered list) 
        represent collection of items

* __Explain how to access and update object properties using dot notation and bracket notation.__

        person = {
            name : "priyank",
            add  : "surat
        }

        person.name = "mali"
        person[add] = "bangalore"

## 9] JavaScript Events

* __What are JavaScript events? Explain the role of event listeners.__
    > when user clicking / typing / hovering in document (browser) what are actions happens in the browser it is called the events.some common enents:

    > `click mouseover keydown submit load scroll`

    > `Event Listener` : is a function that listens a specific events for an element and execute callback fun when the event happens.

* __How does the `addEventListener()` method work in JavaScript? Provide an example__

        <button id="btn">Submit</button>

        <script>
            document.getElementbyId("btn").addEventListener("click",()=>{
                alert("button is clicked");
            })
        </script>

## 10] DOM Manipulation

* __What is the `DOM (Document Object Model)` in JavaScript? How does JavaScript interact with the DOM?__
    > it is represent the structure of document as a hierarchical tree : how each element conencted with each other 

    > DOM represent a document as a tree nodes.root of the tree is document

    > JavaScript interacts with the DOM using the document :

        getElementById
        getElementsByClassName
        getElementsByTagName
        querySelector
        querySelectorAll ...

* __Explain the methods `getElementById()`, `getElementsByClassName()`, and `querySelector()` used to select elements from the DOM.__

    > `getElementById()` : for ID selector

    > `getElementsByClassName()` : return `HTML collection`

    > `querySelector()` : select `first` query of the document
## 11] JavaScript Timing Events (setTimeout, setInterval)

* **Explain the `setTimeout()` and `setInterval()` functions in JavaScript. How are they used for timing events?**

    > for schedule task to execute at perticular time later or repeatedly after a specific interval. 

    > `setTimeout()` : execute callback fn once after a specified delay (in milliseconds)

        setTimeout(()=>{
            console.log("run after 3 second")
        },3000) 

    > `setInterval()` : execute callback fn repeatedly after a specified delay (in milliseconds)

        setInterval(function(){
            console.log("continous run after 3 sec")
        },3000)

* **: Provide an example of how to use `setTimeout()` to delay an action by 2 seconds.**

        setTimeout(()=>{
            console.log("run after 2 second")
        },2000)

## 12] JavaScript Error Handling

* **What is error handling in JavaScript? Explain the `try`, `catch`, and `finally` blockswith an example.**

* **Why is error handling important in JavaScript applications?**
    > to handled unexpected error

    > to manage runtime errors

    > for user and deveopment prespective server should response in proper-way that's why error handling is important