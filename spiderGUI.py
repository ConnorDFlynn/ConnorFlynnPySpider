__author__ = 'Connor'
__author__ = 'Alex'

import webbrowser
import subprocess

from tkinter import * #Importing Tkinter package

class spiderGUI:
    def __init__(self, master):
        url = "http://localhost:5000" #WebUI Local Host Address
        url2 = "http://pyspider.readthedocs.org/en/master/tutorial/" #Tutorial Address

        def OpenUrl():
            try:
                webbrowser.open_new(url) #Open WebUI URL
                master.destroy() #Close window after click
            except:
                pass
            subprocess.Popen("run.bat")

        def OpenUrl2():
            try:
                webbrowser.open_new(url2) #Open Tutorial URL
            except:
                pass

        def window(): #Window Creation Function
            labelfont = ('hel', 12, 'bold') #Label font variable that has preferences for the PySpider label
            label = Label(master, text = 'PySpider Start', bg ='light green') #Create a header label
            label.config(font=labelfont) #Adding fonts
            label.pack() #Placing the label into the Tkinter window

            button = Button(master, fg='red', text = 'Start Here!', command = OpenUrl, font = 'hel') #Create a button that opens localhost
            button.pack(pady=10) #Space in between buttons and placing button in window

            tutButton = Button(master, text = 'Tutorial!', command = OpenUrl2) #Open tutorial URL when button clicked
            tutButton.pack() #Placing the button into the Tkinter window
        window() #Call the window function when SpiderGUI class is called


main = Tk() #TK initialize
main.geometry("350x150")  #Create window that can be re-sized
main.title("Welcome to PySpider!!!") #Create title for window
main.configure(bg='light green') #Make background color light green
gui = spiderGUI(main) #Instance of spiderGUI
main.mainloop() #Call main method that opens up the window with the preferences