# AutoTask
Automate your Tasks with a Simple GUI

# Dev Manual
Used Libs:
 - PySimpleGUI
 - PyAutoGUI
 - Time
 - JSON
 - pynput
 - MultiProcessing

---
 
 The Application is divided between 2 windows:

- MAIN WINDOWS: The main window where you select 2 options: "Exec Automation Task" and "New Automation Task"
- Configure Window: The window where you configure the tasks
  
 ## How does automation code work?

 The code is saved in the `data.json` file, in field `"tasks"` which saves an array of all the code that must be executed.

 When you use the `Exec Automation Task` button the program uses an `eval` to execute the code saved in `data.json`

 When you go to `New Automation Task` and click on a button, the respective button code is saved in a local dictionary which after you close the window is saved in `data.json`

<!-->
# Api
Use python code and extra functionS
<!-->
