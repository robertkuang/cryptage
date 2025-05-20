"""
Module qui contient l'interface graphique de l'application Encryptix.
Cette classe implémente l'interface utilisateur avec Tkinter.
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import webbrowser
from secure_crypt import SecureCrypt

class Application(tk.Tk):
    """
    Classe qui gère l'interface graphique de l'application.
    Hérite de tk.Tk pour créer une fenêtre principale.
    """
    
    def __init__(self):
        """Initialise l'interface graphique de l'application"""
        super().__init__()
        self.title("Encryptix - Logiciel de Cryptage")
        self.geometry("600x400")
        self.secure_crypt = SecureCrypt()
        self.configure(bg="#f0f0f0")
        self.setup_ui()
        
    def setup_ui(self):
        """Configure tous les éléments de l'interface utilisateur"""
        # Style
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
        self.style.configure("TFrame", background="#f0f0f0")
        
        # Cadre principal
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Titre
        title_label = ttk.Label(main_frame, text="Encryptix", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        
        # Description
        description = ttk.Label(main_frame, text="Une solution simple et sécurisée pour crypter vos documents", 
                              wraplength=500, justify="center")
        description.pack(pady=5)
        
        # Cadre de sélection de fichier
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(pady=20, fill=tk.X)
        
        self.file_label = ttk.Label(file_frame, text="Aucun fichier sélectionné")
        self.file_label.pack(side=tk.LEFT, padx=5)
        
        select_button = ttk.Button(file_frame, text="Sélectionner un fichier", command=self.select_file)
        select_button.pack(side=tk.RIGHT, padx=5)
        
        # Cadre de mot de passe
        password_frame = ttk.Frame(main_frame)
        password_frame.pack(pady=10, fill=tk.X)
        
        password_label = ttk.Label(password_frame, text="Mot de passe:")
        password_label.pack(side=tk.LEFT, padx=5)
        
        self.password_entry = ttk.Entry(password_frame, show="*", width=30)
        self.password_entry.pack(side=tk.RIGHT, padx=5, fill=tk.X, expand=True)
        
        # Boutons d'action
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        encrypt_button = ttk.Button(button_frame, text="Crypter", command=self.encrypt_file)
        encrypt_button.pack(side=tk.LEFT, padx=10)
        
        decrypt_button = ttk.Button(button_frame, text="Décrypter", command=self.decrypt_file)
        decrypt_button.pack(side=tk.LEFT, padx=10)
        
        # Statut
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.pack(pady=10)
        
        # Pied de page
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
        footer_text = ttk.Label(footer_frame, text="Encryptix utilise le chiffrement AES 256-bit", font=("Arial", 8))
        footer_text.pack(side=tk.LEFT)
        
        github_link = ttk.Label(footer_frame, text="GitHub", font=("Arial", 8, "underline"), foreground="blue", cursor="hand2")
        github_link.pack(side=tk.RIGHT)
        github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/votre_username/securecrypt"))
    
    def select_file(self):
        """Ouvre une boîte de dialogue pour sélectionner un fichier"""
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier")
        if file_path:
            self.file_label.config(text=os.path.basename(file_path))
            self.file_path = file_path
            self.status_label.config(text="")
    
    def encrypt_file(self):
        """Action pour crypter le fichier sélectionné"""
        if not hasattr(self, 'file_path'):
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier.")
            return
            
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Erreur", "Veuillez entrer un mot de passe.")
            return
            
        try:
            output_file = self.secure_crypt.encrypt_file(self.file_path, password)
            self.status_label.config(text=f"Fichier crypté avec succès: {os.path.basename(output_file)}")
            messagebox.showinfo("Succès", f"Le fichier a été crypté avec succès.\nEmplacement: {output_file}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors du cryptage: {str(e)}")
    
    def decrypt_file(self):
        """Action pour décrypter le fichier sélectionné"""
        if not hasattr(self, 'file_path'):
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier.")
            return
            
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Erreur", "Veuillez entrer un mot de passe.")
            return
            
        try:
            output_file = self.secure_crypt.decrypt_file(self.file_path, password)
            self.status_label.config(text=f"Fichier décrypté avec succès: {os.path.basename(output_file)}")
            messagebox.showinfo("Succès", f"Le fichier a été décrypté avec succès.\nEmplacement: {output_file}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors du décryptage: {str(e)}")