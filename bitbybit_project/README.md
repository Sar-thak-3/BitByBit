<div align="center">
 <img src="./assets/bitbybit.jpg" alt="Banner Image" style="width: 200px; border-radius: 10px;">
</div>

<br>

<h4 align="center">HTML (Hypertext Markup Language) documents to DOCX 
(Microsoft Word) format converter</h4>

<br>
<br>
<div align="center">
  <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 badge" width="110"/>
  <img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="HTML5" width="100"/>
  <img src="https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white" width = "155"/>
  <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" alt="CSS3" width="160"/>
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="JavaScript" width="120" /> 
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Bootstrap" width="125"/>
</div>

<br>

---
# Problem Statement 🎯
Converting HTML (Hypertext Markup Language) documents to DOCX 
(Microsoft Word) format. While both formats serve different purposes, there are scenarios where it's necessary to 
convert HTML content into a more widely used and editable format like DOCX.

---
## Our Focus Areas:
➢ Preserving Formatting and Styles: Maintaining the original formatting, including fonts, colors, styles, and 
layouts, is crucial for the converted document to accurately represent the original HTML content.

➢ Dealing with Hyperlinks and References: Ensuring that hyperlinks, references, and cross-references within the 
HTML document are retained and functional in the resulting DOCX file.

➢ Supporting Complex HTML Structures: Robust handling of complex HTML structures, including nested 
elements, tables, lists, and CSS styles, is necessary for a reliable conversion process.

➢ Minimizing Data Loss: Minimizing the loss of information during the conversion process, such as special 
characters, non-standard fonts, and custom CSS styles.

➢ Scalability and Performance: The conversion tool should be capable of handling large or multiple HTML files 
efficiently without compromising on accuracy or speed.

---
## Implementation:
### Frontend:
We have created a user-friendly form using HTML, CSS, Bootstrap, and JavaScript. The form allows users to upload a file, which is then processed. Once the processing is complete, a downloadable DOCX file is generated. The combination of these technologies ensures a seamless and responsive user experience.

### Backend: 
In the backend of this project, we have implemented a robust system to handle file uploads and processing. Upon receiving a file from the user, it is stored in a designated model. Subsequently, the file undergoes processing and is converted into a DOCX format. Finally, the processed document is promptly sent back to the user via an HTTP response. This backend workflow ensures efficient handling and delivery of processed files, enhancing the overall user experience.

### Background Process
Used various python libraries to comprehensively achieve the best results in the conversion of HTML to Docx. 

---
## Setup 
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Sar-thak-3/BitByBit.git
$ cd bitbybit_project
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ env/scripts/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
