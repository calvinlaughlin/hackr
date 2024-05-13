import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
import time
from threading import Thread
import pygame  # For playing sounds
import os

class PopupGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("+{}+{}".format(
            int((self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2),
            int((self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2)
        ))  # Center the main window
        self.popups = []
        self.game_active = False
        
        # Initialize pygame for sound
        pygame.init()
        pygame.mixer.init()
        
        # Load sound
        self.sound = pygame.mixer.Sound("popups/erro.mp3")  # Adjust path as needed
        
        # Button to start the game
        start_button = tk.Button(root, text="Start Game", command=self.start_game)
        start_button.pack(pady=20)
        
        # Label to show the timer
        self.timer_label = tk.Label(root, text="30", font=("Helvetica", 18))
        self.timer_label.pack()

    def start_game(self):
        if self.game_active:
            return  # Avoid starting a new game if one is already active
        self.game_active = True
        self.timer = 30
        self.update_timer()

        def create_popup(index):
            if index < 20:
                popup = tk.Toplevel(self.root)
                path = f"popups/pop{random.randint(1,4)}.png"
                img = PhotoImage(file=path)  # Adjust path as needed
                img_width, img_height = img.width(), img.height()
                popup.geometry(f"{img_width}x{img_height}+{random.randint(100, 800)}+{random.randint(100, 600)}")
                label = tk.Label(popup, image=img)
                label.image = img  # Keep a reference!
                label.pack(expand=True)
                popup.protocol("WM_DELETE_WINDOW", lambda win=popup: self.close_popup(win))
                self.popups.append(popup)
                
                # Play sound
                self.sound.play()
                
                # Schedule next popup
                delay = random.randint(50, 200)  # Delay
                self.root.after(delay, lambda: create_popup(index + 1))
        
        # Start creating popups with initial index 0
        create_popup(0)
        
        # Start the timer
        Thread(target=self.run_timer).start()

    def close_popup(self, win):
        if win in self.popups:
            self.popups.remove(win)
            win.destroy()
            if not self.popups and self.game_active:
                self.game_active = False
                messagebox.showinfo("Result", "You won!")

    def run_timer(self):
        while self.timer > 0 and self.game_active:
            time.sleep(1)
            self.timer -= 1
            self.timer_label.config(text=str(self.timer))
        if self.game_active:
            self.game_active = False
            for win in self.popups:
                win.destroy()
            self.popups.clear()
            messagebox.showinfo("Time's Up", "You lose!")

    def update_timer(self):
        self.timer_label.config(text=f"Time Remaining: {self.timer}s")
        if self.timer > 0:
            self.root.after(1000, self.update_timer)

# Create the main window
root = tk.Tk()
root.title("Pop-up Game")
app = PopupGame(root)
root.mainloop()
