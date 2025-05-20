"""
Module qui contient la classe SecureCrypt pour les opérations de cryptage et décryptage.
Cette classe implémente les fonctionnalités de chiffrement AES-256 en mode CBC avec une vérification d'intégrité.
"""

import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class SecureCrypt:
    """
    Classe qui gère les opérations de cryptage et décryptage des fichiers
    en utilisant l'algorithme AES-256 bits en mode CBC.
    """
    
    def __init__(self):
        """Initialisation de l'objet de cryptage"""
        self.key = None
        
    def generate_key(self, password):
        """
        Génère une clé AES-256 à partir du mot de passe fourni.
        
        Args:
            password (str): Le mot de passe fourni par l'utilisateur
            
        Returns:
            bytes: Une clé de 32 octets (256 bits)
        """
        # Utilisation de SHA-256 pour créer une clé de 32 bytes (256 bits)
        return hashlib.sha256(password.encode('utf-8')).digest()
    
    def encrypt_file(self, file_path, password):
        """
        Chiffre un fichier avec AES-256 en mode CBC.
        
        Args:
            file_path (str): Chemin du fichier à chiffrer
            password (str): Mot de passe utilisé pour générer la clé
            
        Returns:
            str: Chemin du fichier chiffré
            
        Raises:
            ValueError: Si le fichier n'existe pas ou si le mot de passe est vide.
        """
        if not os.path.exists(file_path):
            raise ValueError("Le fichier spécifié n'existe pas.")
        
        if not password:
            raise ValueError("Le mot de passe ne peut pas être vide.")
        
        # Génération de la clé à partir du mot de passe
        key = self.generate_key(password)
        
        # Génération d'un vecteur d'initialisation (IV) aléatoire
        iv = os.urandom(16)
        
        # Création de l'objet cipher
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # Lecture du fichier à chiffrer
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # Ajout de padding PKCS7 pour que la taille soit un multiple de 16
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        # Chiffrement des données
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Création du fichier chiffré (ajout du suffixe .encrypted)
        output_file = file_path + '.encrypted'
        with open(output_file, 'wb') as f:
            # Écriture de l'IV suivi des données chiffrées
            f.write(iv + encrypted_data)
        
        return output_file
    
    def decrypt_file(self, file_path, password):
        """
        Déchiffre un fichier chiffré avec AES-256.
        
        Args:
            file_path (str): Chemin du fichier à déchiffrer
            password (str): Mot de passe utilisé pour générer la clé
            
        Returns:
            str: Chemin du fichier déchiffré
            
        Raises:
            ValueError: Si le fichier n'existe pas, si le mot de passe est incorrect,
                       ou si le fichier n'est pas un fichier chiffré valide.
        """
        if not os.path.exists(file_path):
            raise ValueError("Le fichier spécifié n'existe pas.")
        
        if not password:
            raise ValueError("Le mot de passe ne peut pas être vide.")
        
        # Génération de la clé à partir du mot de passe
        key = self.generate_key(password)
        
        # Lecture du fichier chiffré
        with open(file_path, 'rb') as f:
            # Les 16 premiers octets sont l'IV
            iv = f.read(16)
            encrypted_data = f.read()
        
        if len(iv) != 16:
            raise ValueError("Le fichier chiffré est corrompu (IV manquant ou invalide).")
        
        # Création de l'objet cipher pour déchiffrer
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        try:
            # Déchiffrement des données
            decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
            
            # Suppression du padding PKCS7
            unpadder = padding.PKCS7(128).unpadder()
            decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
        except ValueError as e:
            raise ValueError("Échec du déchiffrement : mot de passe incorrect ou fichier corrompu.") from e
        
        # Création du fichier déchiffré (suppression du suffixe .encrypted)
        if file_path.endswith('.encrypted'):
            output_file = file_path[:-10]
        else:
            output_file = file_path + '.decrypted'
            
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)
        
        return output_file