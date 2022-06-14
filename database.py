import sqlite3 as sq


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sq.connect('db/installations.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    """
    Initiate the database with all the tables.
    """

    def exc_sql(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        sql_db = open('db/db.sql')
        sql_read = sql_db.read()
        cursor.executescript(sql_read)
        connection.commit()

    # Installations aquatiques

    """
    Add all aquatique installations in the database.
    """

    def add_aquatique(self, id_uev, type_, nom, arrondisse, addresse,
                      propriete, gestion, point_x, point_y, equipeme,
                      long_, lat):
        connection = self.get_connection()

        connection.execute("""INSERT OR REPLACE INTO aquatique(id_uev, type,
                            nom, arrondisse, addresse, propriete, gestion,
                            point_x, point_y, equipeme, long_, lat)
                            VALUES(:id_uev, :type, :nom, :arrondisse,
                            :addresse, :propriete, :gestion, :point_x,
                            :point_y, :equipeme, :long_, :lat)""",
                           {'id_uev': id_uev, 'type': type_, 'nom': nom,
                            'arrondisse': arrondisse, 'addresse': addresse,
                            'propriete': propriete, 'gestion': gestion,
                            'point_x': point_x, 'point_y': point_y,
                            'equipeme': equipeme, 'long_': long_, 'lat': lat})
        connection.commit()

    """
    Get all aquatique installations from a specific arrondissement.
    """

    def get_aquatiques_arrondissement(self, arrondissement):
        cursor = self.get_connection().cursor()
        cursor.execute("""SELECT * FROM aquatique
                       WHERE arrondisse=:arrondissement""",
                       {'arrondissement': arrondissement})
        fetched_aquatiques = cursor.fetchall()
        return [{
                "ID_UEV": ligne[1],
                "TYPE_": ligne[2],
                "NOM": ligne[3],
                "ARRONDISSE": ligne[4],
                "ADRESSE": ligne[5],
                "PROPRIETE": ligne[6],
                "GESTION": ligne[7],
                "POINT_X": ligne[8],
                "POINT_Y": ligne[9],
                "EQUIPEME": ligne[10],
                "LONG": ligne[11],
                "LAT": ligne[12],
                }
                for ligne in fetched_aquatiques
                ]

    """
    Get all aquatique installations ordered by ascending name.
    """

    def get_all_aquatiques(self):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM aquatique ORDER BY nom ASC")
        fetched_installations = cursor.fetchall()
        return [{
                "ID_UEV": ligne[1],
                "TYPE_": ligne[2],
                "NOM": ligne[3],
                "ARRONDISSE": ligne[4],
                "ADRESSE": ligne[5],
                "PROPRIETE": ligne[6],
                "GESTION": ligne[7],
                "POINT_X": ligne[8],
                "POINT_Y": ligne[9],
                "EQUIPEME": ligne[10],
                "LONG": ligne[11],
                "LAT": ligne[12],
                }
                for ligne in fetched_installations
                ]

    """
    Get all aquatique installations with a specific name.
    """

    def get_aquatiques_nom(self, nom):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM aquatique WHERE nom=:nom",
                       {'nom': nom})
        fetched_aquatiques = cursor.fetchall()
        return [{
                "ID_UEV": ligne[1],
                "TYPE_": ligne[2],
                "NOM": ligne[3],
                "ARRONDISSE": ligne[4],
                "ADRESSE": ligne[5],
                "PROPRIETE": ligne[6],
                "GESTION": ligne[7],
                "POINT_X": ligne[8],
                "POINT_Y": ligne[9],
                "EQUIPEME": ligne[10],
                "LONG": ligne[11],
                "LAT": ligne[12],
                }
                for ligne in fetched_aquatiques
                ]
    # Installations aquatiques

    # Glissades
    """
    Add all glissade in the database.
    """

    def insert_glissade(self, nom, nom_arr, cle, date_maj, ouvert,
                        deblaye, condition):

        connection = self.get_connection()
        connection.execute(
            (
                """insert or replace into glissade(nom, nom_arr, cle,
                date_maj, ouvert, deblaye, condition)
                values(?, ?, ?, ?, ?, ?, ?)"""
            ),
            (nom, nom_arr, cle, date_maj, ouvert, deblaye, condition),
        )
        connection.commit()

    """
    Get all glissades from a specific arrondissement.
    """

    def get_glissade_arrondissement(self, arrondissement):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM glissade WHERE nom_arr=:arrondissement",
                       {'arrondissement': arrondissement})
        fetched_installations = cursor.fetchall()
        return [{
                "nom": ligne[1],
                "nom_arr": ligne[2],
                "cle": ligne[3],
                "date_maj": ligne[4],
                "ouvert": ligne[5],
                "deblaye": ligne[6],
                "condition": ligne[7],
                }
                for ligne in fetched_installations
                ]

    """
    Get all glissades ordered by ascending name.
    """

    def get_all_glissades(self):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM glissade ORDER BY nom ASC")
        fetched_installations = cursor.fetchall()
        return [{
                "nom": ligne[1],
                "nom_arr": ligne[2],
                "cle": ligne[3],
                "date_maj": ligne[4],
                "ouvert": ligne[5],
                "deblaye": ligne[6],
                "condition": ligne[7],
                }
                for ligne in fetched_installations
                ]

    """
    Get all glissades with a specific name.
    """

    def get_glissades_nom(self, nom):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM glissade WHERE nom=:nom",
                       {'nom': nom})
        fetched_installations = cursor.fetchall()
        return [{
                "nom": ligne[1],
                "nom_arr": ligne[2],
                "cle": ligne[3],
                "date_maj": ligne[4],
                "ouvert": ligne[5],
                "deblaye": ligne[6],
                "condition": ligne[7],
                }
                for ligne in fetched_installations
                ]
    # Glissades

    """
    Get all aquatique installations and all glissades with a specific name.
    """

    def get_all_names(self):
        cursor = self.get_connection().cursor()
        cursor.execute("""SELECT nom FROM aquatique UNION
                        ALL SELECT nom FROM glissade ORDER BY nom ASC""")
        fetched_names = cursor.fetchall()
        return [ligne[0]for ligne in fetched_names]
