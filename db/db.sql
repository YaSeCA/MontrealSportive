DROP TABLE IF EXISTS aquatique;
DROP TABLE IF EXISTS glissade;
DROP TABLE IF EXISTS compte;

CREATE TABLE aquatique (
  id INTEGER PRIMARY KEY,
  id_uev INTEGER,
  type VARCHAR(255),
  nom VARCHAR(255),
  arrondisse VARCHAR(255),
  addresse VARCHAR(255),
  propriete VARCHAR(255),
  gestion VARCHAR(255),
  point_x VARCHAR(255),
  point_y VARCHAR(255),
  equipeme VARCHAR(255),
  long_ FLOAT,
  lat FLOAT
);

CREATE TABLE glissade (
  id INTEGER PRIMARY KEY,
  nom VARCHAR(255),
  nom_arr VARCHAR(255),
  cle VARCHAR(10),
  date_maj TEXT,
  ouvert VARCHAR(10),
  deblaye VARCHAR(10),
  condition VARCHAR(10)
);

create table compte (
  id integer primary key,
  nom VARCHAR(50),
  courriel VARCHAR(50),
  date_inscription DATE,
  mdp VARCHAR(50)
);


