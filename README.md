# E# (E-Sharp) Programming Language

Le langage **E#** est une réponse directe à la demande de créer un langage de programmation qui soit à la fois **dur, complexe, simple, difficile à coder, robuste et résistant**. Développé en Python, E# est conçu pour être un exercice de style dans la complexité intentionnelle.

## Principes de Conception

| Caractéristique Demandée | Implémentation en E# |
| :--- | :--- |
| **Dur & Complexe** | Syntaxe extrêmement verbeuse (mots-clés multiples pour une seule action), gestion manuelle et obligatoire de la mémoire (`ALLOCATE`/`DEALLOCATE`), et notation préfixée pour les calculs. |
| **Simple** | Le jeu d'instructions est minimaliste (Déclaration, Calcul, Affichage, Sécurité). La complexité réside dans la verbosité, pas dans le nombre de concepts. |
| **Anglais** | Tous les mots-clés sont en anglais (ex: `ESTABLISH`, `TRANSMIT`, `SECURE`). |
| **Robuste & Résistant** | Bloc de gestion d'erreurs obligatoire (`SECURE`/`OTHERWISE`) et variables "résistantes" (`RESISTANT`) qui ne peuvent pas être modifiées après leur initialisation, garantissant une robustesse au niveau des données. |

## Mots-clés et Syntaxe

### 1. Gestion de la Mémoire (Complexité Obligatoire)

Toute exécution doit être précédée d'une allocation et suivie d'une désallocation.

```e_sharp
ALLOCATE MEMORY FOR EXECUTION END
...
DEALLOCATE MEMORY END
```

### 2. Déclaration de Variable (Verbosite)

La déclaration est longue et peut inclure le mot-clé `RESISTANT` pour rendre la variable immuable.

```e_sharp
ESTABLISH INTEGER my_var AS 42 END
ESTABLISH RESISTANT STRING CONSTANT_MSG AS "Do not change" END
```

### 3. Calcul (Complexité de Notation)

Utilise une notation préfixée et verbeuse.

```e_sharp
CALCULATE ADD WITH var1 AND var2 STORE IN result END
CALCULATE SUBTRACT WITH var3 AND 10 STORE IN final_result END
```

### 4. Affichage

```e_sharp
TRANSMIT result TO CONSOLE END
```

### 5. Robustesse et Résistance (Gestion d'Erreurs)

Le bloc `SECURE` est le seul moyen d'exécuter du code. Toute erreur non gérée dans le bloc `SECURE` principal est capturée par `OTHERWISE`.

```e_sharp
SECURE
    # Code à exécuter
OTHERWISE
    # Code à exécuter en cas d'erreur
END
```

## Utilisation de l'Interpréteur

L'interpréteur E# est implémenté dans le fichier `esharp.py`.

```bash
python3 esharp.py <fichier_e_sharp>
```

## Exemple de Code E# (`tutorial.es`)

```e_sharp
SECURE
    TRANSMIT "--- E# Tutorial: The Complex Simplicity ---" TO CONSOLE END
    
    ALLOCATE MEMORY FOR EXECUTION END
    TRANSMIT "Memory successfully allocated." TO CONSOLE END

    ESTABLISH INTEGER BASE_VALUE AS 5 END
    ESTABLISH RESISTANT INTEGER RESISTANCE_FACTOR AS 100 END
    ESTABLISH STRING MESSAGE AS "The result is: " END
    
    CALCULATE ADD WITH BASE_VALUE AND RESISTANCE_FACTOR STORE IN INTERMEDIATE_RESULT END
    
    TRANSMIT MESSAGE TO CONSOLE END
    TRANSMIT INTERMEDIATE_RESULT TO CONSOLE END
    
    SECURE
        TRANSMIT "Attempting to change RESISTANCE_FACTOR..." TO CONSOLE END
        ESTABLISH INTEGER RESISTANCE_FACTOR AS 1 END # This will fail
    OTHERWISE
        TRANSMIT "RESISTANCE_FACTOR is resistant. Error handled gracefully." TO CONSOLE END
    END
    
    DEALLOCATE MEMORY END
    TRANSMIT "Memory successfully deallocated. Program terminated." TO CONSOLE END

OTHERWISE
    TRANSMIT "CRITICAL FAILURE: The entire program failed to execute." TO CONSOLE END
END
```

## Résultat de l'Exécution

L'exécution du code ci-dessus démontre la robustesse et la résistance du langage :

```
--- E# Tutorial: The Complex Simplicity ---
Memory successfully allocated.
The result is: 
105
Attempting to change RESISTANCE_FACTOR...
RESISTANCE_FACTOR is resistant. Error handled gracefully.
Memory successfully deallocated. Program terminated.
```
