Encryptix

Une application simple et sécurisée pour crypter vos fichiers avec AES-256.
Fonctionnalités

    Cryptage et décryptage de fichiers avec AES-256 bits
    Interface utilisateur graphique simple et intuitive
    Plateforme (Windows)
    



    Clonez ce dépôt : git clone https://github.com/robertkuang/cryptage.git

    Lancez l'application : 
    npm run devStart


En suivant ces étapes, tu devrais pouvoir exécuter ton script Python dans GitHub Codespaces sans problème

Utilisation

    Sélectionnez un fichier à crypter ou décrypter
    Entrez un mot de passe
    Cliquez sur "Crypter" ou "Décrypter"
    Le fichier résultant sera créé dans le même dossier que le fichier d'origine

Structure du projet

  

Sécurité

    Utilise l'algorithme de chiffrement AES-256 bits, standard de l'industrie
    Mode CBC (Cipher Block Chaining) avec vecteur d'initialisation (IV) aléatoire
    Dérivation de clé sécurisée à partir du mot de passe via SHA-256




