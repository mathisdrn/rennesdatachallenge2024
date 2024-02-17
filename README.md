# RennesDataChallenge 2024

Le Master Mathématiques Appliquées, Statistique (Universités de Rennes 1 et Rennes 2), le Master Monnaie, Banque, Finance Assurance (Université de Rennes 1), Gwenlake, TAC ECONOMICS et l'association Rennes Data Science, organisent un data challenge les 19 et 20 janvier 2024 à la Faculté des Sciences Economiques de Rennes.

Deux sujets était proposé : 
- ENEDIS : sur le thème de la maintenance préventive
- FederalFinance : prédiction de la valeur des crypto-monnaies au jour le jour.

Ce repositery traite du deuxième sujet.

Le deuxième était accompagné d'un jeu de données : une série temporelle à fréquence jours ouvrés entre le 08-2017 et 03-2023. Ce jeu données contient plus de 300 colonnes : variables économiques, réseaux sociaux (nombre de tweet parlant du BTC, sentiments des tweets).  

## Structure du projet

Les notebooks contenus dans ce repositery traitent le jeux de données et entraîne différents modèles sur celui-ci. 

```
rennesdatachallenge2024
├─ data                     // data files
├─ images                   // prediction and datasets figures  
├─ 00 - Setup.ipynb         // to setup installation of virtual-env and dependencies
├─ 01 - Cleaning.ipynb      // preprocessing of dataset
├─ 02 - EDA.ipynb           // exploratory data analysis
├─ 03 - model.ipynb         // initial implementation of various models (Prophet from Facebook, initial implementation of SARIMAX) 
├─ 04 - VARMAX.ipynb        // VARMAX model implementation
├─ 05 - SARIMAX.ipynb       // SARIMAX model implementation
├─ 06 - SDAE + LSTM.ipynb   // Stacked denoising auto encoder + LSTM implementation
├─ 07 - Result.ipynb        // Analysing performance and KPI of various models
```

## À noter

Ce repositery a été mis à jour à posteriori du challenge.
