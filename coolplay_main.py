import tkinter as tk
from tkinter import font, ttk, PhotoImage, simpledialog, filedialog,messagebox
import time
import side_fuctions
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.paused = False
        self.start_time = None
        self.playing_item_duration = ""
        self.current_item_playing = ""
        self.playing_item_duration_in_seconds = 0


    def play_music(self, file_to_play):
        #print("Play music")
        pygame.mixer.music.load(file_to_play)
        self.start_time = time.time()
        self.paused = False
        pygame.mixer.music.play()

    def stop_music(self):
       #print("Stopping music")
        pygame.mixer.music.stop()
        self.start_time = None
    
    def is_playing(self):
        if pygame.mixer.music.get_busy():
            return True
        else:
            return False

class CoolPlayKabulApp:
    def __init__(self, master):
        # Initialize the application with the master window
        self.master = master
        self.master.title("CoolPlay Kabul")  # Set the title of the window
        self.configure_window()  # Configure window properties

        # Create the object of Music Player
        self.player = MusicPlayer()
        self.player.paused = True
        self.player.playing_item_duration = ""
        self.player.current_item_playing = ""
        self.player.playing_item_duration_in_seconds = 0


        # Status of the Program
        self.status = "Ready"

        # Define fonts for widgets
        self.clock_widget_font = font.Font(family="Digital-7", size=60)
        self.duration_widget_font = font.Font(family="DS-Digital Normal", size=30)

        # Create clock and table widgets
        self.create_clock_widget()
        self.create_table_widget()
        self.create_remaining_widgets()
        self.create_control_widgets()
        self.create_menu()
        self.create_status_bar()

        #checking schedule
        self.check_schedule()  

    def configure_window(self):
        # Configure window resizing
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.minsize(width=800, height=600)  # Set minimum window size
        self.master.iconbitmap(r'C:\Users\Moh_N\Documents\CoolPlay\CoolPlay.ico')  # Set window icon

    def create_clock_widget(self):
        # Create frame for clock widget
        self.label_frame_clock = tk.LabelFrame(self.master, text="Current Time")
        self.label_frame_clock.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        

        # Create clock label widget
        self.clock_widget = tk.Label(self.label_frame_clock, font=self.clock_widget_font, anchor='center')
        self.clock_widget.grid(row=0, column=0, sticky="nsew")
        
        # Configure resizing for clock widget frame
        self.label_frame_clock.columnconfigure(0, weight=1)
        self.label_frame_clock.rowconfigure(0, weight=1)

        self.update_clock()

    def create_table_widget(self):
        # Create table widget
        self.table = ttk.Treeview(self.master, columns=('TIME', 'ITEM', 'DURATION', 'OUTTIME'))
        self.table.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Add column headers to the table
        self.add_table_headers()
        # Configure column widths for the table
        self.configure_columns()


    def add_table_headers(self):
        # Add column headers to the table
        self.table.heading('#0', text='#')
        self.table.heading('#1', text='TIME')
        self.table.heading('#2', text='ITEM')
        self.table.heading('#3', text='DURATION')
        self.table.heading('#4', text='OUTTIME')
        

    def configure_columns(self):
        # Configure column widths for the table
        hash_width = 0.02
        time_width = 0.10
        item_width = 0.60
        duration_width = 0.12
        outtime_width =  0.12
        total_width = self.master.winfo_width()
        self.table.column('#0', width=int(total_width * hash_width))
        #print(int(total_width * hash_width))
        self.table.column('#1', width=int(total_width * time_width))
        #print(int(total_width * time_width))
        self.table.column('#2', width=int(total_width * item_width))
        #print(int(total_width * item_width))
        self.table.column('#3', width=int(total_width * duration_width))
        #print(int(total_width * duration_width))
        self.table.column('#4', width=int(total_width * outtime_width))
        #print(int(total_width * duration_width))
        self.set_table_font()
