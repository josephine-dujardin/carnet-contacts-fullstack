# Mini Carnet de Contacts - Fullstack App

Ce projet est une petite application web pour gérer des contacts (nom, email, téléphone). Elle permet d'afficher une liste de contacts à partir d'une API Python (Flask) dans une interface React, avec MySQL comme base de données.

## Structure

- `frontend/` : Application React (interface utilisateur)
- `backend/` : API Flask (Python) qui communique avec une base de données MySQL et retourne une liste de contacts
- `requirements.txt` : dépendances Python

## 🛠️ Prérequis

Avant de lancer le projet, assurez-vous d'avoir installé :

- [Node.js](https://nodejs.org/) pour le frontend
- [Python](https://www.python.org/) pour le backend
- [MySQL](https://www.mysql.com/) pour la base de données

## 🚀 Lancer le projet

### 1. Backend (Flask)

Dans le répertoire `backend` :

1. Créez une base de données MySQL (par exemple, `carnet_contacts`) et une table `contact` en utilisant les instructions de création SQL fournies dans le projet.
2. Installez les dépendances Python nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurez votre connexion à la base de données MySQL dans le fichier `app.py` (modifiez les informations de connexion selon votre configuration).
4. Lancez le serveur Flask :
   ```bash
   python app.py
   ```

### 2. Frontend (React)

Dans le répertoire `frontend` :

1. Installez les dépendances JavaScript :
   ```bash
   npm install
   ```
2. Lancez l'application React :
   ```bash
   npm start
   ```

### 3. Base de données MySQL

Assurez-vous que votre base de données MySQL est en cours d'exécution et que les informations de connexion dans le backend sont correctes. La table `contact` devrait avoir les champs suivants :

- `id` (clé primaire, auto-incrémentée)
- `name` (varchar)
- `email` (varchar)
- `phone` (varchar)

## Fonctionnalités

- Affichage de la liste des contacts
- Ajout de nouveaux contacts via l'interface web
- Intégration avec une base de données MySQL pour stocker les contacts
