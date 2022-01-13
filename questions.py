# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:51:36 2021

@author: yonau
"""

#attribuer à chaque musique un chiffre ptt
quiz_musique_titre = {
    1 : {'bonnerep': 'La fete', 'prop2': 'On verra bien', 'prop3': "Le mendiant de l'amour", 'prop4': "L'Amerique" },
    2 : {'bonnerep': 'La vie en rose', 'prop2': 'Non je ne regrette rien', 'prop3': 'La grande Zoa', 'prop4': "Les p'tits papiers"},
    3 : {'bonnerep': 'Les yeux de la mama', 'prop2': 'La mama', 'prop3': 'Le temps des fleurs', 'prop4': 'Le temps est bon'},
    4 : {'bonnerep': 'Les 4 saisons', 'prop2': '9 eme symphonie', 'prop3': 'Valse minute', 'prop4': 'Don Giovani'},
    5 : {'bonnerep': 'For me formidable', 'prop2': 'Langue de Shakespeare', 'prop3': 'La bohème', 'prop4': 'La bicyclette'},
    6 : {'bonnerep': 'Mathilde', 'prop2': 'Gertrude', 'prop3': 'Marlène', 'prop4': 'Jojo'}
    }

quiz_question_musique = { 1: 'Amir_La_fete_titre', 2: 'Edith_Piaf_La_Vie_En_Rose_titre', 3: 'Kendji_Girac_Les_yeux_de_la_mama_titre', 
                         4: 'Vivaldi_Quatre_Saisons_titre', 5: 'Charles_Aznavour_For_Me_Formidable_titre', 6: 'Jacques_Brel_Mathilde_est_revenue_titre'}

quiz_les_chanteurs = { 1: 'Amir_La_fete_chanteur', 2: 'Christophe_Aline_chanteur', 3: 'Enrico_Macias_Le_Mendiant_De_Lamour_chanteur', 
                         4: 'Vivaldi_Quatre_Saisons_chanteur', 5: 'Yves_Montand_A_Paris_chanteur', 6: 'Tino_Rossi_Marinella_chanteur'}

quiz_chanteurs_propositions = {
    1 : {'bonnerep': 'Amir', 'prop2': 'Christophe', 'prop3': 'Slimane', 'prop4': 'Joe Dassin' },
    2 : {'bonnerep': 'Christophe', 'prop2': 'Pierre Perret', 'prop3': 'Charles Aznavour', 'prop4': 'Eddy Mitchell'},
    3 : {'bonnerep': 'Enrico Macias', 'prop2': 'Richard Anthony', 'prop3': 'Khaled', 'prop4': 'Ray Charles'},
    4 : {'bonnerep': 'Vivaldi', 'prop2': 'Bethoven', 'prop3': 'Mozart', 'prop4': 'Chopin'},
    5 : {'bonnerep': 'Yves Montand', 'prop2': 'Simone Signoret', 'prop3': 'Georges Michael', 'prop4': 'Daniel Balavoine'},
    6 : {'bonnerep': 'Tino Rossi', 'prop2': 'Henri Salvador', 'prop3': 'Charles Trenet', 'prop4': 'Jcques Dutronc'}
    }

quiz_proverbes = { 1: 'Se croire sorti(e) de la cuisse de ...', 2: 'Mieux vaut être seul que mal...', 3: "On n'est jamais mieux servi que par...", 
                         4: "En matière d'aumône, il faut fermer... et ouvrir le cœur", 5: "L'habit ne fait pas...",
                         6: "Qui a peur est à demi...", 7: "Petit à petit ... fait son nid",
                         8: "Pierre qui roule n'amasse pas ...", 9: "A vaincre sans ..., on triomphe sans gloire",
                         10: "Advienne que...", 11: "Aide- toi et ... t'aidera"
                         }
quiz_proverbes_propositions = {
    1 : {'bonnerep': 'Jupiter', 'prop2': 'Mars', 'prop3': 'Vénus', 'prop4': 'Mercure' },
    2 : {'bonnerep': 'Accompagné', 'prop2': 'Luné', 'prop3': 'Entouré', 'prop4': 'Entouré'},
    3 : {'bonnerep': 'Soi-même', 'prop2': 'Son chat', 'prop3': 'Son ami', 'prop4': 'Son voisin'},
    4 : {'bonnerep': 'La bouche', 'prop2': 'La porte', 'prop3': 'Les yeux', 'prop4': 'La casserole'},
    5 : {'bonnerep': 'Le moine', 'prop2': 'Le riche', 'prop3': 'Le sage', 'prop4': 'Le saint'},
    6 : {'bonnerep': 'Battu', 'prop2': 'Vaincu', 'prop3': 'Perdu', 'prop4': 'Mordu' },
    7 : {'bonnerep': "L'oiseau", 'prop2': 'Le pigeon', 'prop3': "L'âne", 'prop4': 'Le perroquet' },
    8 : {'bonnerep': 'Mousse', 'prop2': 'Grappe', 'prop3': "D'oseille", 'prop4': 'De plomb' },
    9 : {'bonnerep': 'Péril', 'prop2': 'Sueur', 'prop3': 'Risque', 'prop4': 'Succès' },
    10 : {'bonnerep': 'Pourra', 'prop2': 'Voudra', 'prop3': 'Louera', 'prop4': 'Saura' },
    11 : {'bonnerep': 'Le ciel', 'prop2': 'Le bon D ieu', 'prop3': 'Le saint', 'prop4': 'David' }
    }

quiz_drapeaux = {
    1: 'd_Allemagne.png',
    2: 'd_Argentine.png',
    3: 'd_Bresil.png',
    4: 'd_Espagne.png',
    5: 'd_Italie.png',
    6: 'd_Japon.png',
    7: 'd_Liban.png',
    8: 'd_Maroc.png',
    9: 'd_Royaume_Uni.png',
    10: 'd_Russie.png',
    11: 'd_Venezuela.png'
    }

quiz_drapeaux_propositions = {
    1: {'bonnerep': 'Allemagne', 'prop2': 'Belgique'},
    2: {'bonnerep': 'Argentine', 'prop2': 'République Tchèque'},
    3: {'bonnerep': 'Bresil', 'prop2': 'Colombie'},
    4: {'bonnerep': 'Espagne', 'prop2': 'Portugal'},
    5: {'bonnerep': 'Italie', 'prop2': 'Allemagne'},
    6: {'bonnerep': 'Japon', 'prop2': 'Pologne'},
    7: {'bonnerep': 'Liban', 'prop2': 'Canada'},
    8: {'bonnerep': 'Maroc', 'prop2': 'Tunisie'},
    9: {'bonnerep': 'Royaume- Uni', 'prop2': 'Etats- Unis'},
    10: {'bonnerep': 'Russie', 'prop2': 'Finlande'},
    11: {'bonnerep': 'Vénézuela', 'prop2': 'Pérou'}
    }

quiz_films = {
    1: 'Arsene_Lupin.jpg',
    2: 'Chapeau_melon_et_bottes_de_cuir.jpg',
    3: 'Charlie_Chaplin.jpg',
    4: 'Colombo.jpg',
    5: 'Dirty_Dancing.jpeg',
    6: 'James_bond.jpg',
    7: 'La_boum.jpg',
    8: 'La_grande_vadrouille.jpg',
    9: 'Laile_ou_la_cuisse.jpg',
    10: 'Laurel_et_Hardy.jpg',
    11: 'Le_diner_de_cons.jpg',
    12: 'Les_aventures_de_rabbi_Jacob.jpg',
    13: 'Les_demoiselles_de_rochefort.jpg',
    }

quiz_films_propositions = {
    1: {'bonnerep': 'Arsène Lupin', 'prop2': 'Les incorruptibles'},
    2: {'bonnerep': 'Chapeau Melon et Bottes de cuir', 'prop2': "L'arnaqueur"},
    3: {'bonnerep': 'Charlie Chaplin', 'prop2': 'Charlie et \n la chocolaterie'},
    4: {'bonnerep': 'Colombo', 'prop2': 'Inspecteur Barnaby'},
    5: {'bonnerep': 'Dirty Dancing', 'prop2': 'Titanic'},
    6: {'bonnerep': 'James Bond', 'prop2': 'Magnum'},
    7: {'bonnerep': 'La Boum', 'prop2': 'La fête'},
    8: {'bonnerep': 'La Grande Vadrouille', 'prop2': 'Les Gendarmes \n et les Gendarmettes'},
    9: {'bonnerep': "L'aile ou la cuisse", 'prop2': 'Les filles du boucher'},
    10: {'bonnerep': 'Laurel et Hardy', 'prop2': 'Le corniaud'},
    11: {'bonnerep': 'Le dîner de cons', 'prop2': "L'aile ou la cuisse"},
    12: {'bonnerep': 'Les aventures \n de Rabbi Jacob', 'prop2': "Les aventures de \n Marco Polo"},
    13: {'bonnerep': 'Les demoiselles \n de Rochefort', 'prop2': "Les demoiselles \n d'Avignon"}
    }

quiz_culture = {
    1: "Qui a été président de \n la République francaise ?",
    2: "Dans quel film a joué \n Louis de Funès ?",
    3: "Quelle ville se trouve dans \n le sud de la France ?"}

quiz_culture_propositions = {
    1: {'intru': 'Laurent Fabius', 'prop2': 'Georges Pompidou', 'prop3': 'René Coty',
        'prop4': "Valéry Giscard d'Estaing", 'prop5': 'François Mitterrand', 
        'prop6': 'Vincent Auriol', 'prop7': 'Gaston Doumergue'},
    2: {'intru': 'Le cercle rouge', 'prop2': 'La grande Vadrouille ', 'prop3': 'La soupe aux chous ',
        'prop4': "L’avare ", 'prop5': 'Le gendarme se marie ', 
        'prop6': 'Le tatoué', 'prop7': 'Ni vu ni connu '},
    3: {'intru': 'Valenciennes ', 'prop2': 'Cézannes', 'prop3': 'Antibes',
        'prop4': "Cap d’Agde", 'prop5': 'Perpignan', 
        'prop6': 'Avignon', 'prop7': 'Grau-du-Roi '}
        }




 




