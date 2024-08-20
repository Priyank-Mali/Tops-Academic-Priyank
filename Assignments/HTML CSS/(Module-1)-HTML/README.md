1] Are the HTML tags and elements the same thing?

    --> No,HTML tags and elements are not same.
    Tag : is a part of HTML syntax used to   create HTML element.Ex,.. <br>, <p>
    Element : is a combination of opening tag and its content and the closing tag.Ex,..<p>My Name is Priyank</p>

2] What are tags and attributes in HTML?

    --> Tags : are the basic building block for HTML.They are used to create elements in HTML document.Ex,.. <div>, <a>

    --> Attributes : provides additionl information about an element.
    Ex,.. <a herf="https://www.google.com">Open Google</a>
    href is an attribute of <a> tag.
3] What are void elements in HTML?

    --> Void elements are basically that element that do not have closing tags and cannot have any child elements or content.
    Bsically self-closing tags.Ex,.. <img>,<br>,<hr> 
4] What are HTML Entities?

    --> HTML entities are used to represent characters that have special meanings in HTML (like <, >, &, etc.)cannot showd in HTML page directly
    &lt;  -- <
    &gt;  -- >
    &amp; -- &
5] What are different types of lists in HTML?

    --> Ordered List     (<ol>)
    --> Unordered List   (<ul>)
    --> Description List (<dl>) : <dt> for terms and <dd> for descriptions.
6] What is the ‘class’ attribute in HTML?

    --> The class attribute is used to assign one or more class names to an HTML element. Classes can be used to apply CSS styles 
    
    <h1 class="heading">Priyank Mali</h1>
7] What is the difference between the ‘id’ attribute and the ‘class’ attribute of HTML elements?

    --> id : attribute is unique and is used to identify a single element.No two elements should have the same id in an HTML document

    --> class : attribute can be shared by multiple elements. It's used to apply the same style to multiple elements.
8] What are the various formatting tags in HTML?

    --> Formatting tags in HTML are used to change the appearance of the text.

    <b>      : Bold text
    <i>      : Italic text
    <u>      : Underlined text
    <strong> : Strong emphasis(usually rendered as bold)
    <em>     : Emphasis (usually rendered as italic)
    <mark>   : Highlighted text
    <sub>    : Subscript text
    <sup>    : Superscript text
9] How is Cell Padding different from Cell Spacing?

    --> Cell Padding : The space between the cell content and its border. It adds space inside the cell.
    --> Cell Spacing : The space between individual cells in a table. It adds space between the borders of adjacent cells.
10] How can we club two or more rows or columns into a single row or column in an HTML table?

    -->  using the colspan and rowspan attributes.
    --> colspan: Merges multiple columns into a single column.

    --> rowspan: Merges multiple rows into a single row.
11] What is the difference between a block-level element and an inline element?

    --> Block-Level Element: These elements take up the full width available and start on a new line.Ex,.. <div>,<h1>,<p>

    --> Inline Element: These elements take up only as much width as necessary and do not start on a new line.Ex,.. <a>,<span>
12] How to create a Hyperlink in HTML?

    --> with use of <a> tag with the href attribute.Ex,..
    <a herf="https://www.google.com">Open Google</a>
13] What is the use of an iframe tag?

    --> <iframe> tag is used to embed another HTML document within the current document and also used to embed videos, maps, or other web pages.
14] What is the use of a span tag? Explain with example?

    --> The <span> tag is an inline container used to wrap text or other inline elements for styling or scripting purposes without affecting the layout.Ex,..
    <p>python is <span style="color:red;">Dynamic<span> type programmig language</p>
15] How to insert a picture into a background image of a web page?

    -->
    <body style="backgroundp-image: url("image.jpg");">
        content here
    </body>
16] How are active links different from normal links?

    --> CSS pseudo-class is used to style an active link.

    <style>
        a:active{
            color: red;
        }
    </style>

    <a herf="https://www.google.com">Open Google</a>    
17] What are the different tags to separate sections of text?

    --> <br>  : Inserts a line break.
    --> <hr>  : Inserts a horizontal rule (divider).
    --> <p>   : Defines a paragraph.
    --> <div> : Defines a division or section in an HTML document.
    --> <section>, <article>, <nav>, <aside>: HTML5 semantic tags used to define specific sections of a webpage.
18] What is SVG?

    --> (SVG) : Scalable Vector Graphics is an XML-based format for describing two-dimensional vector graphics. It allows for high-quality images that can be scaled indefinitely without losing quality.
19] What is difference between HTML and XHTML?

    --> HTML (HyperText Markup Language): More forgiving in syntax, not case-sensitive, allows omission of some tags and attributes.

    --> XHTML (Extensible HyperText Markup Language): Stricter syntax rules, must be well-formed, case-sensitive, and all tags must be closed properly.
20] What are logical and physical tags in HTML? 

    --> Logical Tags: These tags do not describe the visual appearance but the logical structure or meaning of the text (e.g., <em> for emphasis, <strong> for strong importance).
    
    --> Physical Tags: These tags describe the physical appearance of the text (e.g., <b> for bold, <i> for italic).