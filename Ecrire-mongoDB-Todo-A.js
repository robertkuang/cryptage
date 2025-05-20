const { default: mongoose } = require('mongoose');

// Importation du module MongoClient depuis la bibliothèque 'mongodb'
const MongoClient = require('mongodb').MongoClient;

// ---Todo1----
// Changer l'URL de connexion à la base de données MongoDB avec votre propre URL de connexion
const url = 'mongodb+srv://ousmaneouattara:7TSt0fcDP5iJ5n9e@cluster0.4zbj4au.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0';


// Connexion à la base de données
MongoClient.connect(url).then(client => {
  console.log("Connexion réussie");
  
// Sélection de la base de données 'ma base de données SpaceX'
  const db = client.db('ma-base-de-données-SpaceX');
   

// ---Todo2---
//Ajouter des documents dans la collection 'users' de la base de données 'ma base de données SpaceX' selon les besoins de votre formulaire 
//d'inscription  (https://www.w3schools.com/mongodb/index.php

    const documents = [
      {"name": "toto1", "prénom": "test1", "email": "toto.test@gmail.com", "password": "toto1234567", "message": "bonjour"},
    ];
    


// Insértion des documents dans la collection 'users' de la base de données 'ma base de données SpaceX'
    return db.collection('users').insertMany(documents);
    
  })
  .then(result => {
    console.log(`${result.insertedCount} documents inserted`);
  })
  .catch(err => {
    console.error(err);
  });