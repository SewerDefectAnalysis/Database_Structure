# Database schema for Defect-Level Sewer Pipe Condition Modeling


## Project overview

This repository provides the complete database structure developed for the paper _Data Requirements for Defect-Level Sewer Pipe Condition Modeling: A State-of-the-Art Review on Sewer Deterioration Analysis_. Its purpose is to translate the conceptual Entity–Relationship Diagram (ERD) (see Fig. 5 in the manuscript) into an executable relational schema using Python, ensuring a coherent and well-organized representation of all entities, attributes, and relationships involved in defect-level sewer condition analysis.

The database is implemented using SQLAlchemy, which functions as the Object–Relational Mapper (ORM) to:

* Define each ERD entity as a Python class,
* Specify all attributes with their corresponding data types,
* Manage the relationships between entities within a relational structure.

The schema is designed to:

* Represent the key entities commonly involved in sewer deterioration studies,
* Explicitly store the attributes (fileds) associated with each entity,
* Model the relationships between tables, including one-to-many and many-to-many structures,
* Support future analyses focusing on factors, defects, failures, and additional aspects relevant to sewer system performance.

---

## Repository Contents

`schema.py`

Defines the full relational schema of the database using SQLAlchemy. This file implements every entity in the ERD, organized into the three conceptual sections used in the study:

* **Factors:** contains physical, environmental, climatic, operational, and geospatial factors that influence sewer deterioration.
* **Defects:** stores inspection events (e.g., CCTV) and defect-level observations extracted from these inspections.
* **Failures:** records failure events affecting the sewer system, including their causes, impacts, and connection to pipe interventions.

It defines all attributes, data types, primary keys, foreign keys, and the complete set of one-to-many and many-to-many relationships.

---

`database.py`

Handles the database configuration and creation process. It includes:

* The SQLite engine definition,
* The session factory (`SessionLocal`) used to interact with the database,
* The `create_tables()` function, which generates all tables defined in `schema.py`.

This file does not define entities; it simply initializes the database and manages the connection.

---

`Database_Creation_and_Usage.ipynb`

A demonstration notebook showing how to interact with the implemented database. It includes:

* Code to run `create_tables()` and generate the database file,
* A command to display the full path of the created SQLite database,
* Example (commented) code for loading Excel files into pandas and uploading them to the corresponding tables.

This notebook serves as a practical guide for users who want to populate or explore the database once the schema has been created.

---

## Requirements

To run the database schema and interact with the relational models, the following Python packages are required:

* Python 3.8+
* SQLAlchemy – used to define the relational schema and manage ORM operations
* pandas – required for working with tabular data before uploading it into the database
* Jupyter Notebook (optional) – only needed to run the example notebook

**Optional dependencies:**

These libraries are only needed depending on the user’s data source:

* openpyxl – required only when loading Excel (.xlsx) files into pandas

* Other readers (e.g., pyarrow, fiona) may be needed if the user imports data from formats such as Parquet, GeoPackage, or others.

Install the main dependencies using:
```
pip install sqlalchemy pandas 
```

If you plan to load Excel files:
```
pip install openpyxl
```

---

## How to Create the Database

To generate the database structure and create all tables defined in the ERD, run the `create_tables()` function from the `database.py` module.

**1. Import and run the table creation function**
```
from database import create_tables

create_tables()
```

This will create the file `sewer_database.db` in the project directory (unless a different path is specified in the database URL).

**2. (Optional) View the full path of the generated database**

If you want to confirm where the SQLite file was created, run:

```
from database import engine
import os

print(os.path.abspath(engine.url.database))
```

**3. Result**

After running these commands:

1. All entities defined in `schema.py` will be created as tables,
3. All relationships (one-to-many and many-to-many) will be enforced through foreign keys,
5. The database will be ready to receive data from CSV, Excel, or other structured formats.

---

## Loading Data Into the Database

Once the database has been created, data can be inserted into any of the tables defined in the schema. Data must first be loaded into a pandas DataFrame, regardless of the original file format (CSV, Excel, Parquet, etc.). After that, it can be uploaded into the corresponding SQL table.

**1. Load your data into a pandas DataFrame**

You can load data from different formats. Here are some common examples:

**CSV:**
```
import pandas as pd

df = pd.read_csv("path/to/file.csv")
```

**Excel (.xlsx):**
```
import pandas as pd

df = pd.read_excel("path/to/file.xlsx", sheet_name=0)
```

**Parquet:**
```
import pandas as pd

df = pd.read_parquet("path/to/file.parquet")
```

**2. Upload the DataFrame into a SQL table**

To upload data, import the corresponding SQLAlchemy model from `schema.py` and use your helper function (e.g., `upload_dataframe_to_table`) along with the SQL engine defined in `database.py`:
```
from schema import Pipe        # Import the target table
from database import engine     # Database engine

upload_dataframe_to_table(df, Pipe, engine)
```

This function will map each column in the DataFrame to the attributes defined in the model and insert all rows into the table.

**3. Example: Loading pipes data**
```
import pandas as pd
from schema import Pipe
from database import engine

# Load data
pipes_df = pd.read_excel("documents/PIPES.xlsx")

# Upload to the database
upload_dataframe_to_table(pipes_df, Pipe, engine)
```

**4. Notes**

The DataFrame must contain columns that match the attribute names in the SQLAlchemy model.

* Missing values (NaN) will be inserted as NULL.
* Additional preprocessing (type conversions, renaming columns) can be performed before uploading.
* This process can be repeated for any entity in the ERD (e.g., Manhole, Inspection, Defect, Failure, etc.).

---

## Extend or adapt the schema (optional)

If necessary, you can modify or expand the database structure by updating `schema.py`:

* Add new attributes
* Add new entities
* Create additional relationships
* Change data types

After modifying the schema, run `create_tables()` again to regenerate the structure.

---

## Citation

If you use this database structure, the ERD, or any component of this repository in your research, please cite the corresponding paper:

González, M. A., Herrán, J., van Zyl, J. E., & Henning, T. F. P. (2025). 
Data Requirements for Defect-Level Sewer Pipe Condition Modeling: A State-of-the-Art Review. _Journal of Water Resources Planning and Management_.

---

## License

This project is distributed under the MIT License.
See the `LICENSE` file for the full text.

---

## Contact

For questions, feedback, or collaboration inquiries related to the paper or this database structure, please contact the corresponding author:

**María A. González**  
Email: _mgon869@aucklanduni.ac.nz_  
Affiliation: University of Auckland
