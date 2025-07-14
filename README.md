# 3-platform to-do app
- I wrote an app that runs on 3 platforms - a CLI client, a GUI client and a Web page.<br>
- All have somehow the same functionalities: add, edit, show, complete and exit
- This application helped me deepen my understanding on <b>working with external files, data types, internal and external libraries and ellaborate a general logic for the code, that can be used in various cases.</b>
# for the CLI client
- We have the following functionalities - add, edit show, complete and exit. Each of the operation have a simple logic, with 'add' you can add new tasks in a file that stores all tasks, 'edit' and 'complete'
requires the indices of the tasks to-do. 'Edit' modify an existing task and 'complete' takes it out of the list of tasks. 'Show' operation displays a list of all the tasks. There is no sorting done on the list, they are displayed and operated in the order in which they were added.
- The functionality of the operations can be seen here:
<img width="1018" height="442" alt="cli" src="https://github.com/user-attachments/assets/d3f78c54-4486-4451-98d9-fa5f3616525f" />
<br><b>'Add' operation</b><br>
<img width="757" height="203" alt="cli - add" src="https://github.com/user-attachments/assets/bf9639ed-a2a6-41fe-b3fb-3648a2c86269" />
<br><b>'Show' operation</b><br>
<img width="628" height="260" alt="cli - show" src="https://github.com/user-attachments/assets/b14d5aae-01ce-4cbc-892f-2518c674362a" />
<br><b>'Edit' operation</b><br>
<img width="565" height="315" alt="cli - edit" src="https://github.com/user-attachments/assets/7043b7ab-f109-4f7e-838c-10e4e96038cf" />
<br><b>'Complete' operation</b><br>
<img width="632" height="203" alt="cli - complete" src="https://github.com/user-attachments/assets/3b283996-9815-4b56-938e-95f98ba2966c" />
<br><b>'Exit' operation</b><br>
<img width="561" height="132" alt="cli - exit" src="https://github.com/user-attachments/assets/5b908bc9-ff56-4185-a9c5-e70d276dc4cc" />
<br><br><br>

# for the GUI client
- I have used <b>FreeSimpleGui</b> module to create a simple GUI that incorporate 3 buttons, one for 'Add', one for 'Edit' and one for 'Complete'. The logic behind each button is pretty simple, as it can be seen in the code.
The functionalities are similar with the ones in the CLI, but they are displayed in a cooler manner, using a graphical user interface. It was a bit more challenging, but I managed to overcome each problem I encountered
and it works as expected.
- The GUI looks like:
<img width="1195" height="742" alt="gui - dashboard" src="https://github.com/user-attachments/assets/01574ae6-bf79-44c8-b983-8d61b8666e53" />
<br><br><br>

# for the Web client
- I have used <b>Streamlit</b> library to create a Web application that reflects the functionalities presented above, especially the 'Add', 'Show' and 'Complete' functionality. I have used the Streamlit documentation to
understand better the assignment and I implemented in a simple manner the page that you'll see below. Basically the tasks will be read from the file and displayed as checkboxes, that later can be completed by clicking on them.
- There is also a text input where you can add a new task to be added to the current tasks list.
- The logic behind the code is simple, but I managed to learn the fundamentals of the <b>Streamlit</b> library.
- The Web interface can be seen below:
 <img width="1615" height="866" alt="web page" src="https://github.com/user-attachments/assets/7aaf4a0a-032d-4da1-acbc-a6ae8517fb63" />
