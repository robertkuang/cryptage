// Importation du module MongoClient depuis la bibliothèque 'mongodb'
const MongoClient = require('mongodb').MongoClient;

// ---Todo1----
// Changer l'URL de connexion à la base de données MongoDB avec votre propre URL de connexion
const url = 'mongodb+srv://ousmaneouattara:7TSt0fcDP5iJ5n9e@cluster0.4zbj4au.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0';

// Connexion à la base de données
MongoClient.connect(url)
  .then(client => {

    // Sélection de la base de données 'ma base de données SpaceX'
    const db = client.db('ma-base-de-données-SpaceX');

    // Sélection de la collection "users"
    const collection = db.collection('users');

    // Utilisation de find pour récupérer tous les documents de la collection
    return collection.find({}).toArray();
  })
  .then(documents => {
    // Affichage des documents récupérés
    console.log('Documents récupérés:');
    documents.forEach(document => {
    console.log(JSON.stringify(document, null, 2)); // Indentation de 2 espaces
    });
  })
  .catch(err => {
    // En cas d'erreur, affichage de l'erreur
    console.error(err);
  });
