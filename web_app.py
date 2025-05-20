"""
Module optionnel pour une version web de l'application.
Ce fichier implémente une interface web avec Flask.
Pour l'utiliser, décommentez le code et exécutez ce fichier.
"""

# Pour utiliser ce module, vous devez installer Flask:
# pip install flask

from flask import Flask, render_template, request, send_file, redirect, url_for
import tempfile
import uuid
import os
from werkzeug.utils import secure_filename
from secure_crypt import SecureCrypt

def create_web_app():
    """
    Crée et configure l'application web Flask
    
    Returns:
        Flask: L'application Flask configurée
    """
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    
    # Dossier temporaire pour les fichiers
    UPLOAD_FOLDER = tempfile.mkdtemp()
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max
    
    secure_crypt = SecureCrypt()
    
    @app.route('/')
    def index():
        """Page d'accueil de l'application web"""
        return render_template('index.html')
    
    @app.route('/encrypt', methods=['POST'])
    def encrypt():
        """Endpoint pour le cryptage de fichiers"""
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        password = request.form['password']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and password:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            try:
                output_file = secure_crypt.encrypt_file(file_path, password)
                return send_file(output_file, as_attachment=True)
            except Exception as e:
                return f"Erreur: {str(e)}", 500
    
    @app.route('/decrypt', methods=['POST'])
    def decrypt():
        """Endpoint pour le décryptage de fichiers"""
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        password = request.form['password']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and password:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            try:
                output_file = secure_crypt.decrypt_file(file_path, password)
                return send_file(output_file, as_attachment=True)
            except Exception as e:
                return f"Erreur: {str(e)}", 500
    
    return app

def main():
    """
    Point d'entrée pour lancer l'application web
    """
    app = create_web_app()
    app.run(debug=True)

if __name__ == "__main__":
    main()
