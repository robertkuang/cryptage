SecureCrypt

Une application simple et sécurisée pour crypter vos fichiers avec AES-256.
Fonctionnalités

    Cryptage et décryptage de fichiers avec AES-256 bits
    Interface utilisateur graphique simple et intuitive
    Multiplateforme (Windows, macOS, Linux)
    Portabilité : peut être exécuté directement ou transformé en exécutable autonome

Installation
Option 1 : Installation directe (nécessite Python)

    Clonez ce dépôt ou téléchargez-le

    Lancez l'application : 
    python web_app.py

Option 2 : Utiliser l'exécutable (aucune installation requise)

    Téléchargez l'exécutable depuis la section Releases
    Double-cliquez sur l'exécutable pour lancer l'application
    OU  exécute cette commande : /dist/main
    Assure-toi que le fichier est exécutable en vérifiant ses permissions : chmod +x dist/main

En suivant ces étapes, tu devrais pouvoir exécuter ton script Python dans GitHub Codespaces sans problème

Utilisation

    Sélectionnez un fichier à crypter ou décrypter
    Entrez un mot de passe
    Cliquez sur "Crypter" ou "Décrypter"
    Le fichier résultant sera créé dans le même dossier que le fichier d'origine

Structure du projet

    main.py : Point d'entrée de l'application
    secure_crypt.py : Implémentation des fonctionnalités de cryptage/décryptage
    gui.py : Interface graphique utilisateur
    web_app.py : Version web de l'application (optionnelle)

Sécurité

    Utilise l'algorithme de chiffrement AES-256 bits, standard de l'industrie
    Mode CBC (Cipher Block Chaining) avec vecteur d'initialisation (IV) aléatoire
    Dérivation de clé sécurisée à partir du mot de passe via SHA-256

Dépendances

    Python 3.6+
    cryptography
    tkinter (inclus dans la plupart des installations Python)


