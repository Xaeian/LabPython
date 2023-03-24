from database import Database




DBNAME = "iot"

conn = Database(host="localhost", user="root", password="sqrt")

conn.Exec(f"DROP DATABASE IF EXISTS {DBNAME};")
conn.Exec(f"CREATE DATABASE {DBNAME};")
conn.db = DBNAME
conn.Exec("""
CREATE TABLE devices (
  id INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
  uid CHAR(24) NOT NULL,
  name VARCHAR(255),
  measurement_interval INT UNSIGNED NOT NULL DEFAULT 5,
  transceive_interval INT UNSIGNED NOT NULL DEFAULT 60,
  PRIMARY KEY (id)
);             
""")
conn.Exec("""
CREATE TABLE data (
  id INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
  device_id INT UNSIGNED NOT NULL,
  time DATETIME NOT NULL,
  temperature FLOAT,
  humidity FLOAT,
  voltage FLOAT,
  PRIMARY KEY (id),
  FOREIGN KEY (device_id) REFERENCES devices(id),
  INDEX device_time (device_id, time)
);         
""")


# "CREATE DATABASE databasename;"