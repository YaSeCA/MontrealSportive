from flask import Flask, request, render_template, g, redirect
from flask import make_response, Response, jsonify

import sqlite3 as sq
from database import Database

import pandas as pd

import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import dicttoxml

import atexit
import warnings

from apscheduler.schedulers.background import BackgroundScheduler
from tzlocal import get_localzone

import urllib
import xml.etree.ElementTree as ET
import urllib.parse


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
warnings.filterwarnings("ignore")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.route("/")
def home():
    return render_template('accueil.html')


# A1
"""
Download the files from the URLs and parse theme to a panda dataframe.
Then add the data to the database.
"""


@app.route("/get-data")
def download_data():
    with app.app_context():
        aquatique = (
            "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-"
            "e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/"
            "download/piscines.csv"
        )

        glissade = (
            "http://www2.ville.montreal.qc.ca/services_citoyens/"
            "pdf_transfert/L29_GLISSADE.xml"
        )

        get_db().exc_sql()

        aquatique_array = parse_aquatique(aquatique)
        add_aquatique_to_db(aquatique_array)

        list_glissade = urllib.request.urlopen(glissade).read()
        tree_glissade = ET.fromstring(list_glissade)
        createListGlissade(tree_glissade)

        return redirect("/"), 200


# A2
"""
Data import from point A1 is done automatically
every day at midnight using a BackgroundScheduler.
"""
# def hello_world():
#     print("Hello World!")


"""
Prints in console the data from the DB.
Replace the function download_data() with verify()
in add_job(), then change the hour/minuite/second
values to try the background scheduler.
"""


@app.route("/try-scheduler")
def verify():
    array = pd.DataFrame(get_db().get_all_aquatiques())
    print(array)
    return render_template('accueil.html')


timeZone = get_localzone()


sched = BackgroundScheduler(timezone=timeZone)
sched.add_job(download_data, 'cron', hour='00', minute='00', second='00')
sched.start()


@atexit.register
def terminate():
    print('Server ended')
    lambda: sched.shutdown()


# A3
"""
Shows the documentation for all REST APIs.
"""


@app.route("/doc")
def doc():
    return render_template("doc.html")


# A4
"""
Returns a JSON array of all the facilities from a specified area.
"""


@app.route("/api/installations", methods=['GET'])
def get_install_where_arrondissement():
    arrondissement = request.args.get("arrondissement")

    if arrondissement is None:
        error_msg1 = True
        return render_template('404.html', error_msg1=error_msg1), 404
    else:
        aquatiques = get_db().get_aquatiques_arrondissement(arrondissement)
        glissades = get_db().get_glissade_arrondissement(arrondissement)
        if len(aquatiques) & len(glissades):
            response = {
                "Installations_Aquatiques": aquatiques,
                "Glissades": glissades
            }
        elif len(aquatiques):
            response = {
                "Installations_Aquatiques": aquatiques
            }
        elif len(glissades):
            response = {
                "Glissades": glissades
            }
        else:
            error_msg2 = True
            return render_template('404.html', error_msg2=error_msg2,
                                   arrondissement=arrondissement), 404

    return jsonify(response), 200


# A6
"""
Returns a JSON array of all the facilities of a specified name.
"""


@app.route("/api/installation-nom", methods=['GET'])
def get_install_where_name():
    nom = request.args.get("nom")

    if nom is None:
        error_msg1 = True
        return render_template('404.html', error_msg1=error_msg1), 404
    else:
        aquatiques = get_db().get_aquatiques_nom(nom)
        glissades = get_db().get_glissades_nom(nom)
        if len(aquatiques) & len(glissades):
            response = {
                "Installations_Aquatiques": aquatiques,
                "Glissades": glissades
            }
        elif len(aquatiques):
            response = {
                "Installations_Aquatiques": aquatiques,
            }
        elif len(glissades):
            response = {
                "Glissades": glissades
            }
        else:
            error_msg4 = True
            return render_template('404.html', error_msg2=error_msg4,
                                   nom=nom), 404

    return jsonify(response), 200


"""
Returns a JSON array of all the facilities of a specified name.
"""


@app.route("/names")
def get_all_names():
    names = get_db().get_all_names()
    return jsonify(names), 200


# C1
"""
Returns a JSON array of all the facilities of a specified type.
"""


@app.route("/api/installation-type", methods=['GET'])
def get_install_where_type():
    type_ = request.args.get("type")

    if type_ is None:
        error_msg1 = True
        return render_template('404.html', error_msg1=error_msg1), 404
    elif type_ == "aquatique":
        installations = get_db().get_all_aquatiques()
        if installations:
            response = {
                "Installations_Aquatiques": installations
            }
        else:
            error_msg3 = True
            return render_template('404.html', error_msg3=error_msg3,
                                   type_=type_), 404
    elif type_ == "glissade":
        installations = get_db().get_all_glissades()
        if installations:
            response = {
                "Glissades": installations
            }
        else:
            error_msg3 = True
            return render_template('404.html', error_msg3=error_msg3,
                                   type_=type_), 404
    else:
        error_msg1 = True
        return render_template('404.html', error_msg1=error_msg1,
                               type_=type_), 404

    return jsonify(response), 200


# C2
"""
Returns a XML file of all the facilities of a specified type.
"""


@app.route("/api/installation-type-xml", methods=['GET'])
def get_install_type_xml():
    type_ = request.args.get("type")

    if type_ is None:
        error_msg1 = True
        return render_template('404.html', error_msg1=error_msg1), 404
    elif type_ == "aquatique":
        installations = get_db().get_all_aquatiques()
    elif type_ == "glissade":
        installations = get_db().get_all_glissades()
    else:
        error_msg1 = True
        return render_template('404.html', error_msg1=error_msg1,
                               type_=type_), 404

    if installations:
        xmlData = dicttoxml.dicttoxml(installations)
        parsedXML = parseString(xmlData)
        xmlFile = parsedXML.toprettyxml(indent="\t",
                                        newl='\n', encoding="utf-8")
        response = Response(xmlFile, mimetype="text/xml")
        response.headers.set("Installations sportives", "text/xml")
    else:
        error_msg3 = True
        return render_template('404.html', error_msg3=error_msg3,
                               type_=type_), 404

    return response, 200


# C3
"""
Returns a CSV file of all the facilities of a specified type.
"""


@app.route("/api/installation-type-csv", methods=['GET'])
def get_install_type_csv():
    type_ = request.args.get("type")

    if type_ is None:
        error_msg1 = True
        return render_template('404.html', error_msg1=error_msg1), 404
    elif type_ == "aquatique":
        installations = get_db().get_all_aquatiques()
    elif type_ == "glissade":
        installations = get_db().get_all_glissades()
    else:
        error_msg1 = True
        return render_template('404.html', error_msg1=error_msg1,
                               type_=type_), 404

    if installations:
        csvData = pd.DataFrame(installations)
        response = make_response(csvData.to_csv(sep=",",
                                                na_rep="MISSING",
                                                header=True,
                                                index=False,
                                                encoding="utf-8",
                                                line_terminator="\n"))
    else:
        error_msg3 = True
        return render_template('404.html', error_msg3=error_msg3,
                               type_=type_), 404

    return response, 200


"""
Parses a CSV file contening data of aquatique facilities into a panda
dataframe.

Parameters:
- url : url to a CSV document
"""


def parse_aquatique(url):
    columns = ['ID_UEV', 'TYPE', 'NOM', 'ARRONDISSE', 'ADRESSE', 'PROPRIETE',
               'GESTION', 'POINT_X', 'POINT_Y', 'EQUIPEME', 'LONG', 'LAT']

    aquatique_array = pd.read_csv(url, names=columns, header=None)
    # remove the first line and column
    aquatique_array = aquatique_array.iloc[1:, :]
    # print(aquatique_array)
    return aquatique_array


"""
Fills the aquatique SQLite table in db.sql with data from a panda
dataframe.

Parameters:
- array : a panda array
"""


def add_aquatique_to_db(array):
    for i in array.index:
        id_uev = array['ID_UEV'][i]
        type_ = array['TYPE'][i]
        nom = array['NOM'][i]
        arrondisse = array['ARRONDISSE'][i]
        addresse = array['ADRESSE'][i]
        propriete = array['PROPRIETE'][i]
        gestion = array['GESTION'][i]
        point_x = array['POINT_X'][i]
        point_y = array['POINT_Y'][i]
        equipeme = array['EQUIPEME'][i]
        long_ = array['LONG'][i]
        lat = array['LAT'][i]
        get_db().add_aquatique(id_uev, type_, nom, arrondisse, addresse,
                               propriete, gestion, point_x, point_y,
                               equipeme, long_, lat)


"""
Fills the glissade SQLite table in db.sql with data from a parsed XML
file.

Parameters:
- tree_glissade : the root of the XML tree
"""


def createListGlissade(tree_glissade):
    db = get_db()
    for row in tree_glissade.findall("glissade"):
        nom = row.find("nom").text
        nom_arr = row.find("arrondissement").find("nom_arr").text
        cle = row.find("arrondissement").find("cle").text
        date_maj = row.find("arrondissement").find("date_maj").text
        ouvert = row.find("ouvert").text
        deblaye = row.find("deblaye").text
        condition = row.find("condition").text
        db.insert_glissade(nom, nom_arr, cle, date_maj,
                           ouvert, deblaye, condition)

        # print(db.get_all_glissades())

    return None


# Error handling
@app.errorhandler(400)
def error_400_handler(e):
    defaut = True
    return render_template('400.html', defaut=defaut), 400


@app.route("/400")
def error_400():
    defaut = True
    return render_template('400.html', defaut=defaut), 400


@app.errorhandler(404)
def error_404_handler(e):
    defaut = True
    return render_template('404.html', defaut=defaut), 404


@app.route("/404")
def error_404():
    defaut = True
    return render_template('404.html', defaut=defaut), 404


@app.errorhandler(500)
def error_500_handler(e):
    defaut = True
    return render_template('500.html', defaut=defaut), 500


@app.route("/500")
def error_500():
    defaut = True
    return render_template('500.html', defaut=defaut), 500


if __name__ == "__main__":
    app.run(debug=True)
