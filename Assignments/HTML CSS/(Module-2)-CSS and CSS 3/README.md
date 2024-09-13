1] What are the benefits of using CSS?

    --> Using CSS we can seprate content and design.HTML is for structure and CSS for apperearance (layout/design)
    --> Easier maintenance
    --> Responsive design

2] What are the disadvantages of CSS?

    --> Complexity with large projects
    --> Different browsers may interpret CSS differently

3] What is the difference between CSS2 and CSS3?

    --> CSS2
    --> not support responsive design
    --> Cannot build 3D animation and media queries, transformation

    --> CSS3
    --> Support responsive design
    --> Supports animation and 3D transformations.

4] Name a few CSS style components

    --> Selectors
    --> Properties
    --> Values
    --> Media queries,...

5] What do you understand by CSS opacity?

    --> Opacity is for transparency level of an element.
    --> from 0 to 1

6] How can the background color of an element be changed?

    --> <h1>Hello World</h1>

    h1{
     background-color: red;
    }

7] How can image repetition of the backup be controlled?

    --> using backgrond-repeat property
    backgrond-repeat: repeat;     (default)
    backgrond-repeat: no-repeat;
    backgrond-repeat: repeat-x;   (repeats horizontally) 
    backgrond-repeat: repeat-y;   (repeats vartically)

8] What is the use of the background-position property?

    --> background-position property controls the position of a backgrond image within an element.

    background-position: center;
    background-position: top;
    background-position: left;
    background-position: bottom;

    or coordinates (e.g., 50px 100px)

9] Which property controls the image scroll in the background?

    --> background-attachment

    scroll (image scrolls with the page),
    fixed  (image stays in place),
    local  (scrolls within the element).


10] Why should background and color be used as separate properties?

    --> background: property used to define the background of an element, including the background color, image, position, and repeat behavior.

    --> color: property is specifically for setting the color of the text or content within an element.
    
    For example, you might want to change the text color without affecting the background or vice versa.

11] How to center block elements using CSS1?

    --> <h1></h1>

    h1{
        width: 50%;
        height: 20px;
        border: 1px solid black;
        margin: auto;
    }

12] How to maintain the CSS specifications?

    --> seprate css file 
    --> proper naming convaction
    --> use css preprocessor like sass or less


13] What are the ways to integrate CSS as a web page?

    --> Inline CSS    (within the element)
    --> Internal CSS  (within the head section using style tag)
    --> External CSS  (seperate style.css file and link it to index.html using link tag )

14] What is embedded style sheets?

    --> Embedded (Internal) style sheets are defined within the <style> tag inside the <head> section of an HTML document.

15] What are the external style sheets?

    --> External style sheets are separate .css files linked to HTML pages. It allow to apply the same styles across multiple pages of a website.

16] What are the advantages and disadvantages of using external style sheets?

    --> Advatages:
    * Easy to maintain and update
    * Faster page loading due to browser caching.

    --> Disadvantage
    * Requires additional HTTP requests.
    * Slight delay in rendering as the external file needs to be loaded.

17] What is the meaning of the CSS selector?

    --> Selectors used to target and apply styles to specific HTML elements. 
    --> Example: p selects all <p> elements, .class-name selects elements with the specified class.

18] What are the media types allowed by CSS?

    --> Screen  : (for devices with screen)
    --> Print   : (for printed materials)
    --> Speech  : (for screen readers)
    --> All     

19] What is the rule set? 

    --> CSS rule set contains one or more selectors and one or more declarations.

    <p>Hello World</p>

    p{
        color: green;
        background-color: yellow;
        font-size: 14px;
        border: 1px solid black;
    }
