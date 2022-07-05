# Présentation du cours
Dans le cadre du cours Programmation Web avancée, nous ont été introduites les méthodes avancées et les bonnes pratiques de conception et de développement d'applications Web modernes. Entre autres : infrastructure et cadre de développement Web ; intégration d'une base de données ; authentification ; conception de services web ; formats de sérialisation ; gestion d'erreurs ; interopérabilité ; déploiement de services ; tests de charge ; sécurité et patrons d'attaques spécifiques aux applications web.

# Description du travail
Il s'agit d'un site web permettant de trouver des installations sportives (aquatiques et glissades) dans la ville de Montréal. Le projet consiste à récupérer un ensemble de données provenant de la ville de Montréal et d'offrir des services (REST) à partir de ces données. 

# Les technologies/APIs utilisées
Python 3, SQLite 3, JavaScript, CSS 3, HTML 5, Jinja, ...

# Comment utiliser le site web

## Méthode #1

Vous pouvez tout simplement aller au lien suivant : https://montrealsportive.herokuapp.com/

## Méthode #2 (pour consulter et éditer)

Installations et manipulations requises : 

1. pip3 install virtualenv
2. virtualenv env
3. source env/bin/activate
4. pip3 install flask flask-sqlalchemy
5. pip install -r requirements.txt

Pour ouvrir le site web dans un furteur :
1. make
2. ouvrir le lien (normalement http://127.0.0.1:5000/)

# Sources
## Sources des images
- static/images/sheep.jpg : https://opensanctuary.org/article/building-a-good-home-for-sheep/
- static/images/mtl.jpg : 
https://journalmetro.com/actualites/montreal/1834430/carte-les-resultats-du-scrutin-dans-les-regions-de-montreal-et-quebec/
https://www.parcjeandrapeau.com/fr/complexe-aquatique-piscines-baignade-competitions-montreal/
https://www.timeout.com/fr/montreal/que-faire/patiner-montreal
https://estmediamontreal.com/sites-glissade-pour-hiver-est/
- static/images/data-center-fire.jpeg : https://www.colocationamerica.com/blog/data-centers-and-fire-how-to-not-go-up-in-flames
- static/images/confused.jpeg : free of rights


## Sources des logos
- https://www.sportloisirmontreal.ca/
- https://reseau-urls.quebec/
- https://tmvpa.com/developpement-moteur
- https://www.patinermontreal.ca/f/paysagee/patin-libre/sports-dequipe
- https://www.desjardins.com/
- https://www.parcjeandrapeau.com/fr/

## Inspiration design :
- https://www.youtube.com/watch?v=gXLjWRteuWI&ab_channel=DesignCourse
- https://www.youtube.com/watch?v=D-h8L5hgW-w&t=12s&ab_channel=DesignCourse

## Autres références
### Fetch API 
- https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

### Heroku (41:30)
- https://youtu.be/Z1RJmh_OqeA?t=2490

### W3schools Align Images Side By Side
- https://www.w3schools.com/howto/howto_css_images_side_by_side.asp

### XML parsing 
- https://docs.python.org/3/library/xml.etree.elementtree.html

### Connexion et s'enregistrer
- https://www.w3schools.com/howto/howto_css_login_form.asp
