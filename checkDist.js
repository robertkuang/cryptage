// checkDist.js
const fs = require('fs');
const path = './dist';

try {
  const stats = fs.statSync(path);
  if (stats.isDirectory()) {
    // Lecture du dossier
    const files = fs.readdirSync(path);
    if (files.length === 0) {
      console.log('Le dossier dist est vide.');
    } else {
      // Simule “ls -la”
      files.forEach(name => {
        const info = fs.statSync(path + '/' + name);
        const isDir = info.isDirectory() ? 'd' : '-';
        const size = info.size.toString().padStart(8, ' ');
        const mtime = info.mtime.toISOString().replace(/T/, ' ').slice(0, 19);
        console.log(`${isDir}rw-r--r--  1 dev dev ${size} ${mtime} ${name}`);
      });
    }
  } else {
    console.log('“dist” existe mais ce n’est pas un dossier.');
  }
} catch (err) {
  if (err.code === 'ENOENT') {
    console.log('Pas de fichier dans dist/'); // équivalent de votre echo
  } else {
    console.error('Erreur inattendue :', err);
    process.exit(1);
  }
}
