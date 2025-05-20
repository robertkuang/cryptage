require('dotenv').config();
console.log("URI MongoDB =", process.env.MONGO_URI);
console.log("Email =", process.env.EMAIL_USER);
/*************************************************************************
*   Chargement des modules nécessaires au fonctionnement du serveur      *
*                et Configuration du serveur express                     *                                                                                                 *
**************************************************************************/

// Chargement des modules nécessaires au fonctionnement du serveur
const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const nodemailer = require('nodemailer');


const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
     user: process.env.EMAIL_USER,
     pass: process.env.EMAIL_PASS
}
});
// Configuration du serveur express
const app = express();

app.use(express.static('.'));
app.use(bodyParser.json());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Définir la route http://127.0.0.1:3000/ pour index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Le serveur Express écoute sur le port 3000
app.listen(3000, () => {
    console.log('Le serveur est en écoute sur le port 3000');
});




/*********************************************************************
*  --Todo 1--   Connexion à la base de données MongoDB (SpaceX)      *                                                                                             
*                                                                    *      ---commit -m "Todo 1"---
* Document ressource:   https://mongoosejs.com/docs/connections.html *                                                                                                                                           
**********************************************************************/

// Connexion à la base de données
mongoose.connect(process.env.MONGO_URI)

/********************************************************************************
*  --Todo 2--      Vérification de la connexion à la base de données SpaceX     *                                                                                         
*                                                                               *       ---commit -m "Todo 2"---
* Document ressource:   https://youtu.be/V8dYGNfHjfk?si=1TEKPUPoA8ayLmEs        *                                                                                                                                           
*********************************************************************************/

// Vérification de la connexion à la base de données
.then(()=>{
  console.log("mongodb connected");
})
.catch(()=>{
  console.log("failed to connect");
})




  /********************************************************************************
  *  --Todo 3--      Création du model schema pour la collection users            *                                                                                         
  *                   !!!!! Vous n'avez qu'à compléter le schema !!!!!            *     ---commit -m "Todo 3"---
  * Document ressource:   https://mongoosejs.com/docs/guide.html                  *                                                                                                                                           
  *********************************************************************************/
  
  // Création du model schema pour la collection users 
  // Complétez le modéle selon les besoins de votre formulaire 

  const userSchema=new mongoose.Schema({
    name:String,
    firstName:String,
    email:String,
    password:String,
  })
  

  // Création du model mongoose pour l'intereaction avec la base de données SpaceX (https://mongoosejs.com/docs/api/model.html#Model())
  const User = mongoose.model('User', userSchema);
  
    
  /*****************************************************************************************************************************
  *  --Todo 4--      Création d'une route HTTPavec la méthode "POST" pour récupérer les données du formulaire d'inscription    *                                                                                         
  *                                                                                                                            *   ---commit -m "Todo 4"---
  * Document ressource:   https://docs.google.com/presentation/d/1cQR0cyTpMT2oYpIXWPNOmK55C_Fr8fycB5ApvrytADY/edit?usp=sharing *                                                                                                                                           
  ******************************************************************************************************************************/
  
  // Définition de l'itinéraire d'inscription et chargement de données à partir du formulaire d'inscription
  
    app.post('/signup', async (req, res) => {
        let name = req.body.name;
        let firstName = req.body.firstName;
        let email = req.body.email;
        let password = req.body.password;


  /****************************************************************************************
  *  --Todo 4-1--       Vérifiez que tous champs du formulaire sont complétés             *   ---commit -m "Todo 4-1"---                                                                                      
  *                                                                                       *
  *****************************************************************************************/
   
  // Vérification des champs requis
    if (!name || !firstName || !email || !password)
        return res.status(400).send('Tous les champs doivent être remplis');
    



  /********************************************************************************
  *  --Todo 4-2--                Créez un nouvel utilisateur                      *      ---commit -m "Todo 4-2"---                                                                                     
  *                                                                               *                                                                                                                                  
  *********************************************************************************/

     // Vérifie si un utilisateur avec le même email existe déjà
    const existingUser = await User.findOne({ email: email });
    if (existingUser) {
        return res.status(409).send('Cet adresse e-mail est déjà utilisée.');
    }

    // Création d'un nouvel utilisateur
    const newUser = new User({
        name: name,
        firstName: firstName,
        email: email,
        password: await bcrypt.hash(password, 10),
});
-

  /********************************************************************************
  *  --Todo 4-3--   Enregistez le nouveau utilisateur dans la base de données     *            ---commit -m "Todo 4-3"---                                                                             
  *                                                                               *                                                                                                                                          
  *********************************************************************************/

    // Sauvegarde du nouvel utilisateur dans la base de données
    
    await newUser.save();


  /*********************************************************************************
  *  --Todo 4-4--  Affichez sur la console un message pour une inscription réussie *        ---commit -m "Todo 4-4"---                                                                                    
  *                Redérigiez l'utilisateur vers la page "inscription-réussie"     *
  **********************************************************************************/

// Redirection vers la page d'inscription réussie
  const mailOptions = {
      from: 'ous93600@gmail.com',
      to: email,
      subject: 'Confirmation d\'inscription',
      text: `Bonjour ${firstName},\n\nMerci pour votre inscription sur notre site !\n\nCordialement,\nL'équipe SpaceX`
  };

  transporter.sendMail(mailOptions, (error, info) => {
    console.log(`Tentative d'envoi de mail à : ${email}`);
      if (error) {
          console.error('Erreur lors de l\'envoi du mail :', error);
      } else {
          console.log('E-mail envoyé : ' + info.response);
      }
 });
  console.log("Enregistrement réussie");
  return res.redirect('index2.html');

});
/*});
  /******************************************************************************************************************** 
  *  --Todo 5--  Création d'une route HTTPavec la méthode "POST" pour vérifier les données du formulaire de connexion *                                                                                         
  *                                                                                                                   *    ---commit -m "Todo 5"---
  * Document ressource:  Maintenant c'est à vous de coder la partie singin                                            *                                                                                                                                           
  *********************************************************************************************************************/

  app.post('/signin', async (req, res) => {
    const { email, password } = req.body;

    // Vérifie que les champs ne sont pas vides
    if (!email || !password) {
        return res.status(400).send('Email et mot de passe requis.');
    }

    try {
        // Recherche l'utilisateur dans la base de données
        const user = await User.findOne({ email: email });

        if (!user) {
            return res.status(401).send('Utilisateur non trouvé.');
        }

        // Vérifie si le mot de passe correspond
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return res.status(401).send('Mot de passe incorrect.');
        }

        res.redirect(`/index2.html`);


        
    } catch (error) {
        console.error(error);
        return res.status(500).send('Erreur du serveur.');
    }
});
