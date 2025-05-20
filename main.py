"""
Fichier principal qui lance l'application SecureCrypt.
Ce fichier importe les autres modules et démarre l'interface utilisateur.
"""

import os
from secure_crypt import SecureCrypt
from gui import Application

def main():
    """
    Fonction principale qui démarre l'application.
    """
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()