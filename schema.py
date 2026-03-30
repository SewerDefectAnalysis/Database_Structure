"""
Database schema for Defect-Level Sewer Pipe Condition Modeling
==============================================================

Code Structure
--------------
The code is organized into three main sections:

Section 1: Factors
    Contains physical, environmental, climatic, operational, and geospatial
    factors that influence sewer deterioration.

Section 2: Defects
    Stores inspection events (e.g., CCTV) and defect-level observations
    extracted from these inspections.

Section 3: Failures
    Records failure events affecting the sewer system, including their causes,
    impacts, and connection to pipe interventions.
"""

"""
Section 1: Factors
==================

This section defines the factor-related entities of the ERD.
These entities describe the physical, environmental, and operational context
of each sewer pipe. The following entities are included:
"""

# Imports and Base Class Definition
from sqlalchemy import (
    Column, Integer, String, Float, Date, DateTime, ForeignKey,Boolean
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

"""
1. Pipe Entity
"""

class Pipe(Base):
    """
    Represents a sewer pipe in the network. This entity contains physical,
    environmental, installation, and contextual attributes describing the
    conditions under which each pipe operates.
    """

    __tablename__ = "pipe"

    # -------------------------
    # PRIMARY KEY
    # -------------------------
    # Unique pipe identification number
    Pipe_ID = Column(Integer, primary_key=True)

    # -------------------------
    # ATTRIBUTES
    # -------------------------

    # Year in which the pipe was installed
    Installation_year = Column(Integer, nullable=True)

    # Nominal internal diameter of the pipe (mm)
    Diameter = Column(Integer, nullable=True)

    # Construction material of the pipe (e.g., PVC, PE, VC, AC, CONC, etc.)
    Material = Column(String(20), nullable=True)

    # Distance between upstream and downstream manholes (m)
    Pipe_length = Column(Float, nullable=True)

    # Average vertical distance from ground level to the pipe crown (m).
    # This value is typically derived from available survey or asset data and may
    # depend on upstream and downstream depth measurements when provided.
    Depth = Column(Float, nullable=True)

    # Depth at the upstream manhole (m).
    # Represents the vertical distance from ground level to the pipe invert/crown
    # at the upstream node. Used as input to estimate overall pipe depth.
    UP_depth = Column(Float, nullable=True)

    # Depth at the downstream manhole (m).
    # Represents the vertical distance from ground level to the pipe invert/crown
    # at the downstream node. Together with upstream depth, it can be used to
    # characterize the depth profile along the pipe.
    DW_depth = Column(Float, nullable=True)

    # Gradient of the pipe from upstream to downstream manhole (%)
    Slope = Column(Float, nullable=True)

    # Type of fluids handled by the pipe (e.g., wastewater, stormwater)
    Sewage_type = Column(String, nullable=True)

    # Elevation of groundwater measured from the pipe (m)
    Groundwater_level = Column(Float, nullable=True)

    # Type of human activity at the pipe location (land use)(e.g., residential, business)
    Land_use=Column(String, nullable=True)

    # Type of human activity at the pipe location (land cover)(e.g., Mixed, Vegetation)
    Land_cover = Column(String, nullable=True)

    # Number of trees within a user-defined buffer around the pipe
    Trees_nearby = Column(Integer, nullable=True)

    # Cross-sectional shape of the pipe (e.g.,circular, oviform)
    Shape = Column(String, nullable=True)

    # Type of support material placed beneath and around the pipe (e.g.,A-concrete, B-well compacted granular material)
    Bedding = Column(String, nullable=True)

    # Type of joint used to connect pipe segments (e.g., Mortar joint, Rubber ring)
    Joint_type = Column(String, nullable=True)

    # Number of residents served by the pipe catchment
    Population = Column(Integer, nullable=True)

    # Climatic characteristics of the area where the pipe is located
    # (This parameter may be represented using climatic indices such as the Thornthwaite Moisture Index (TMI)
    # or the Southern Oscillation Index (SOI), or other relevant parameters depending on data availability and regional context)
    Climatic_condition = Column(Float, nullable=True)

    # Classification of the sewer system (e.g., Transmission, Local)
    Sewer_category = Column(String, nullable=True)

    # Number of property connections to the pipe
    Sewer_connections = Column(Integer, nullable=True)

    # Identifier of the nearest weather station
    Weather_station_ID = Column(Integer, nullable=True)

    # Water quality condition based on chemical, physical, and biological parameters
    # (Depend on each indicator. If more indicators are added, each will have its own unit.)
    Water_quality = Column(Float, nullable=True)

    # Material used to fill the trench around the pipe
    Backfill_type = Column(String, nullable=True)

    # Expected service life of the pipe according to design standards (years)
    Design_life = Column(Integer, nullable=True)

    # Technique used to install the pipe (e.g., Trench, Trenchless)
    Installation_method = Column(String, nullable=True)

    # Company that produced the pipe
    Manufacturer = Column(String, nullable=True)

    # Pipe wall thickness (mm)
    Wall_thickness = Column(Float, nullable=True)

    #Coating of the pipe
    Coating=Column(String, nullable=True)

    # Assessed quality or condition of the installation work
    # (This parameter can be reported at different stages of the construction process. It may include written comments or
    # inspection notes from which relevant information can later be extracted.)
    Construction_quality = Column(String, nullable=True)

    # Indicates if the area experiences freeze–thaw cycles
    Frost_action = Column(Boolean, nullable=True)

    # Ground surface elevation from DEM (m)
    Ground_level = Column(Float, nullable=True)

    # Type of internal lining used for rehabilitation (e.g., CIPP, PVC liner)
    Lining_type = Column(String, nullable=True)

    # Condition when flow exceeds pipe capacity
    Surcharge = Column(Boolean, nullable=True)

    # Indicates if the pipe is affected by tidal fluctuations
    Tidal_influence = Column(Boolean, nullable=True)

    # Number of commercial properties connected to the pipe
    No_of_commercial_properties = Column(Integer, nullable=True)

    # Number of upstream users directly connected
    No_of_direct_upstream_users = Column(Integer, nullable=True)

    # Identifier of the seismic activity characteristics near the pipe
    Seismic_activity_ID = Column(Integer, nullable=True)

    # -------------------------
    # SOIL PROPERTIES (GEOSPATIAL RELATIONSHIP)
    # -------------------------

     # Soil acidity or alkalinity (pH value)
    Soil_pH = Column(Float, nullable=True)

    # Soil classification type (e.g., clay, silt, sand, loam)
    Soil_type = Column(String, nullable=True)

    # Soil moisture content or moisture classification
    Soil_moisture = Column(String, nullable=True)

    # Electrical resistivity of the soil (ohm·m), related to corrosion risk
    Soil_resistivity = Column(Float, nullable=True)

    # -------------------------
    # SURFACE LOAD (GEOSPATIAL RELATIONSHIP)
    # -------------------------

    #Intensity of vehicle load acting on the surface above the pipe
    Traffic_load=Column(String, nullable=True)

    #Is there a municipal road running or crossing  over the pipe?
    Road_above=Column(Boolean, nullable=True)

    #Does the pipe pass under a building?
    Building_above=Column(Boolean, nullable=True)

    # Relationships to factor entities (one pipe -> one or many records)
    Weather_station_ID = Column(Integer, ForeignKey("weather_station.Weather_station_ID"))

    # Upstream manhole identifier (FK)
    Manhole_up_ID = Column(
        Integer,
        ForeignKey("manhole.Manhole_ID"),
        nullable=True,
    )

    # Downstream manhole identifier (FK)
    Manhole_down_ID = Column(
        Integer,
        ForeignKey("manhole.Manhole_ID"),
        nullable=True,
    )

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # One weather station can be associated with many pipes
    weather_station = relationship("WeatherStation", back_populates="pipes")

    # Upstream and downstream manholes (each manhole may be linked to many pipes)
    upstream_manhole = relationship(
        "Manhole",
        foreign_keys=[Manhole_up_ID],
        back_populates="pipes_upstream",
    )

    # Relationship to downstream manhole (one manhole -> many downstream pipes)
    downstream_manhole = relationship(
        "Manhole",
        foreign_keys=[Manhole_down_ID],
        back_populates="pipes_downstream",
    )

    # One-to-one relationship: each pipe has a single hydraulic properties record
    hydraulic_properties = relationship(
        "HydraulicProperties",
        back_populates="pipe",
        uselist=False,
    )

    # One-to-many relationship: a pipe can have multiple intervention records
    interventions = relationship(
        "InterventionHistory",
        back_populates="pipe",
    )

    # One-to-many relationship: a pipe can have multiple failure records
    failures = relationship(
        "Failure",
        back_populates="pipe",
    )

    # One-to-many relationship: each pipe can have a many seismic impact record
    seismic_impacts = relationship(
        "PipeSeismicImpact",
        back_populates="pipe",
        cascade="all, delete-orphan",
    )
    # One-to-many relationship: a pipe can have multiple inspection records
    inspection = relationship(
        "Inspection",
        back_populates="pipe",
    )

"""
 2. Weather_station Entity
_____
"""

class WeatherStation(Base):
    """
    Weather station associated with one or more pipes and climate
    observations (rainfall, air humidity, air temperature).
    """
    __tablename__ = "weather_station"

    # Unique identifier of the weather station (primary key)
    Weather_station_ID = Column(Integer, primary_key=True)

    # X coordinate of the weather station location (e.g. NZTM, UTM, etc.)
    X_coordinate = Column(Float, nullable=True)

    # Y coordinate of the weather station location
    Y_coordinate = Column(Float, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # One weather station can be linked to many pipes
    pipes = relationship("Pipe", back_populates="weather_station")

    # One weather station can have many air temperature records
    air_temperature_records = relationship(
        "AirTemperature",
        back_populates="weather_station",
    )

    # One weather station can have many air humidity records
    air_humidity_records = relationship(
        "AirHumidity",
        back_populates="weather_station",
    )

    # One weather station can have many rainfall records
    rainfall_records = relationship(
        "Rainfall",
        back_populates="weather_station",
    )


class Rainfall(Base):
    """
    Rainfall observations associated with a weather station. Each record
    corresponds to rainfall statistics measured at a given time.
    """
    __tablename__ = "rainfall"

    # Weather station where the rainfall was observed (FK + part of the PK)
    Weather_station_ID = Column(
        Integer,
        ForeignKey("weather_station.Weather_station_ID")
    )

    rainfall_id = Column(Integer, primary_key=True, autoincrement=True)

    # Date (and optionally time) when the rainfall measurement or aggregation period ended.
    Observation_time = Column(Date)

    # Time interval or aggregation period of rainfall observation. (e.g. hourly, daily, monthly)
    Frequency = Column(String, nullable=True)

    # Type of statistical value represented by the record. (e.g. mean, max, min)
    Statistics = Column(String, nullable=True)

    # Amount of rainfall recorded per unit time, or cumulative rainfall depth during the observation period.
    Intensity = Column(Float, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------
    weather_station = relationship(
        "WeatherStation",
        back_populates="rainfall_records",
    )


class AirHumidity(Base):
    """
    Air humidity observations associated with a weather station.
    """
    __tablename__ = "air_humidity"

    air_humidity_id = Column(Integer, primary_key=True)

    # Weather station where humidity was observed (FK)
    Weather_station_ID = Column(
        Integer,
        ForeignKey("weather_station.Weather_station_ID")
    )

    # Date (and optionally time) when the air humidity was observed or recorded
    Observation_time = Column(Date)

    # Time interval or aggregation period of the observation (e.g. hourly, daily, monthly)
    Frequency = Column(String, nullable=True)

    # Type of statistical value represented by the record (e.g. mean, max, min)
    Statistics = Column(String, nullable=True)

    # Recorded air humidity value for the corresponding period and station (e.g. relative humidity in %)
    Humidity_value = Column(Float, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------
    weather_station = relationship(
        "WeatherStation",
        back_populates="air_humidity_records",
    )


class AirTemperature(Base):
    """
    Air temperature observations associated with a weather station.
    """
    __tablename__ = "air_temperature"

    # Weather station where temperature was observed
    Weather_station_ID = Column(
        Integer,
        ForeignKey("weather_station.Weather_station_ID")
    )

    air_temperature_id = Column(Integer, primary_key=True, autoincrement=True)

    # Date (and optionally time) when the air temperature was observed or recorded
    Observation_time = Column(Date)

    # Time interval or aggregation period of the observation(e.g. hourly, daily, monthly)
    Frequency = Column(String, nullable=True)

    # Type of statistical value represented by the record (e.g. mean, max, min)
    Statistics = Column(String, nullable=True)

    # Recorded air temperature value for the corresponding period and station (°C)
    Temperature_value = Column(Float, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------
    weather_station = relationship(
        "WeatherStation",
        back_populates="air_temperature_records",
    )

"""
## 3. Seismic_activity Entity
___
"""
class PipeSeismicImpact(Base):

    __tablename__ = "pipe_seismic_impact"

    # -------------------------
    # PRIMARY KEY
    # -------------------------
    # Unique identifier of the seismic activity record
    Pipe_ID = Column(
        Integer,
        ForeignKey("pipe.Pipe_ID"),
        nullable=False,
    )

    Seismic_activity_ID = Column(
        Integer,
        ForeignKey("seismic_activity.Seismic_activity_ID"),
        nullable=False,
    )

    id = Column(Integer, primary_key=True, autoincrement=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # One seismic impact record belongs to a single pipe
    pipe = relationship(
        "Pipe",
        back_populates="seismic_impacts",
    )

    # Many pipe-seismic-impact records can reference the same seismic activity
    seismic_activity = relationship(
        "SeismicActivity",
        back_populates="pipe_impacts",
    )

class SeismicActivity(Base):
    """
    Seismic activity information associated with the area where the pipe is located.
    This table stores attributes related to seismic events
    that characterize the exposure of pipes to earthquake-related effects.
    """

    __tablename__ = "seismic_activity"

    # -------------------------
    # PRIMARY KEY
    # -------------------------
    # Unique identifier of the seismic activity record
    Seismic_activity_ID = Column(Integer, primary_key=True)

    # -------------------------
    # SEISMIC ATTRIBUTES
    # -------------------------

    # Type of seismic event recorded in the area near the pipe network. (e.g., earthquake)
    Seismic_type = Column(String, nullable=True)

    # Date (and optionally time) on which the seismic event occurred
    Reference_date = Column(Date, nullable=True)

    # Measure of the energy released by the seismic event, usually expressed
    # in the Richter or moment magnitude scale. (e.g., moment magnitude Mw)
    Magnitude = Column(Float, nullable=True)

    # Depth below the ground surface where the seismic event originated (km)
    Depth_km = Column(Float, nullable=True)

    # X-coordinate of the seismic event epicenter.
    X_coordinate = Column(Float, nullable=True)

    # Y-coordinate of the seismic event epicenter.
    Y_coordinate = Column(Float, nullable=True)

    #the maximum acceleration experienced by the ground during an earthquake, expressed
    # as a fraction or percentage of the acceleration due to gravity (g).
    peak_ground_acceleration = Column(Float, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # Many pipe-seismic-impact records can reference the same seismic activity
    pipe_impacts = relationship(
        "PipeSeismicImpact",
        back_populates="seismic_activity",
    )

"""
## 4. Manhole Entity
____________
"""
class Manhole(Base):
    """
    Represents a manhole structure in the sewer network. Manholes act as
    access points for maintenance and inspection, and serve as connection
    nodes between pipes.

    Pipes reference manholes through:
    - Manhole_up_ID   (upstream end of the pipe)
    - Manhole_down_ID (downstream end of the pipe)
    """
    __tablename__ = "manhole"

    # -------------------------
    # PRIMARY KEY
    # -------------------------
    # Unique manhole identification number
    Manhole_ID = Column(Integer, primary_key=True)

    # -------------------------
    # MANHOLE ATTRIBUTES
    # -------------------------

    # X coordinate of downstream manhole. (e.g., NZTM, UTM, etc.)
    X_coordinate = Column(Float, nullable=True)

    # Y coordinate of downstream manhole.
    Y_coordinate = Column(Float, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # Pipes whose upstream end is this manhole
    pipes_upstream = relationship(
        "Pipe",
        foreign_keys="Pipe.Manhole_up_ID",
        back_populates="upstream_manhole",
    )

    # Pipes whose downstream end is this manhole
    pipes_downstream = relationship(
        "Pipe",
        foreign_keys="Pipe.Manhole_down_ID",
        back_populates="downstream_manhole",
    )

"""
## 5. Hydraulic_properties Entity
____
"""
class HydraulicProperties(Base):
    """
    Hydraulic performance indicators for a pipe. This table stores
    flow and velocity values derived from hydraulic models, as well
    as the estimated pipe capacity.

    The relationship with Pipe is one-to-one: each pipe has at most
    one HydraulicProperties record, identified by the same Pipe_ID.
    """
    __tablename__ = "hydraulic_properties"

    # -------------------------
    # PRIMARY KEY / FOREIGN KEY
    # -------------------------
    # Pipe identifier (also primary key) linking directly to the Pipe table
    Pipe_ID = Column(
        Integer,
        ForeignKey("pipe.Pipe_ID"),
        primary_key=True,
    )

    # -------------------------
    # HYDRAULIC ATTRIBUTES
    # -------------------------

    # The maximum flow rate recorded or estimated in the sewer during wet weather conditions (m3/s)
    Wet_peak_flow_rate = Column(Float, nullable=True)

    # The maximum flow rate recorded or estimated in the sewer under dry weather conditions (m3/s)
    Dry_peak_flow_rate = Column(Float, nullable=True)

    # The highest velocity of flow measured or simulated in the sewer during wet weather conditions (m/s)
    Wet_peak_velocity = Column(Float, nullable=True)

    # The highest velocity of flow measured or simulated in the sewer during dry weather conditions (m/s)
    Dry_peak_velocity = Column(Float, nullable=True)

    # Estimated flow capacity of the pipe (m3/s)
    Pipe_capacity = Column(Float, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # One hydraulic record belongs to a single pipe (one-to-one)
    pipe = relationship(
        "Pipe",
        back_populates="hydraulic_properties",
    )

"""
## 6. Intervention_history Entity
____
"""
class InterventionHistory(Base):
    """
    Records of maintenance, repair, or renewal interventions carried out on pipes.
    Each record describes one intervention applied to a specific pipe over a
    defined length and time period.
    """
    __tablename__ = "intervention_history"

    # -------------------------
    # PRIMARY KEY
    # -------------------------
    # Unique identifier of the intervention record
    Intervention_ID = Column(Integer, primary_key=True, autoincrement=True)

    # -------------------------
    # TEMPORAL INFORMATION
    # -------------------------

    # Date when the intervention work began.
    Start_date = Column(Date, nullable=True)

    # Date when the intervention was completed.
    End_date = Column(Date, nullable=True)

    # -------------------------
    # INTERVENTION ATTRIBUTES
    # -------------------------

    # Description of the type of intervention performed. (e.g., cleaning, repair, relining)
    Type_of_intervention = Column(String, nullable=True)

    # Indicates whether the intervention was part of a planned maintenance program or performed in response to an unexpected failure. (e.g., reactive, planned)
    Planned_or_reactive = Column(String, nullable=True)

    # Current status of the intervention. (e.g., completed, in progress, cancelled)
    Status = Column(String, nullable=True)

    # Priority level assigned to the intervention, typically based on urgency or risk. (e.g., low, medium, high)
    Priority = Column(String, nullable=True)

    # Identifier of the pipe where the intervention was carried out (FK)
    Pipe_ID = Column(
        Integer,
        ForeignKey("pipe.Pipe_ID"),
        nullable=False,
    )

    # Longitudinal position (distance along the pipe) where the intervention begins, measured from the upstream end (m)
    Position_start = Column(Float, nullable=True)

    # Longitudinal position (distance along the pipe) where the intervention ends (m)
    Position_end = Column(Float, nullable=True)

    # Additional notes or remarks describing the intervention.
    Comments = Column(String, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # Many interventions can be associated with the same pipe
    pipe = relationship(
        "Pipe",
        back_populates="interventions",
    )

    failures = relationship(
        "Failure",
        back_populates="intervention",
    )

"""
# Section 2: Defects
==================

This section defines the Defect-related entities shown in the ERD.
These entities describe the inspection records and the individual defects
observed along each pipe.
"""

"""
## 1. Inspection
______
"""
class Inspection (Base):
    """
    Represents a CCTV or inspection carried out on a specific pipe.
    Each record describes one inspection event, including its date, coverage
    length, status and an overall condition rating.
    """

    __tablename__='inspection'

    #--------------------
    # Primary-Key
    #--------------------

    #Unique identifier for each inspection record.
    Inspection_ID=Column(Integer,primary_key=True)

    #Foreign key linking the inspection to the corresponding pipe that was surveyed.
    Pipe_ID=Column(Integer, ForeignKey("pipe.Pipe_ID"),nullable=False)

    # -------------------------
    # INSPECTION ATTRIBUTES
    # -------------------------

    # Date when the inspection was carried out
    Date = Column(Date, nullable=True)

    # Overall condition rating assigned to the pipe based on this inspection
    Condition_rating = Column(Integer, nullable=True)

    # Length of pipe that was inspected (m)
    Survey_length = Column(Float, nullable=True)

    # Status of the inspection (e.g., completed, in progress, cancelled)
    Inspection_status = Column(String, nullable=True)

    #The direction in which the CCTV was made (e.g.,upstream, downstream)
    Inspection_direction=Column(String, nullable=True)

    #Additional notes recorded by the operator or analyst regarding the inspection conditions or anomalies.
    Comments=Column(String, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # Many inspections belong to one pipe (Pipe 1 -> N Inspections)
    pipe = relationship(
        "Pipe",
        back_populates="inspection",
    )

    # One inspection can have many defects (Inspection 1 -> N Defects)
    defects = relationship(
        "Defect",
        back_populates="inspection",
    )

"""
## 2. Defect
______
"""
class Defect(Base):
    """
    Represents a single defect observed during an inspection. Each record
    includes the main defect code, characterization, quantification and
    the position of the defect along the pipe.
    """
    __tablename__ = "defect"

    # -------------------------
    # PRIMARY KEY
    # -------------------------

    # Unique identifier of the defect record
    Defect_ID = Column(Integer, primary_key=True, autoincrement=True)

    # -------------------------
    # RELATIONSHIP TO INSPECTION
    # -------------------------

    # Foreign key linking the defect record to the corresponding  inspection where the defect was observed.
    Inspection_ID = Column(
        Integer,
        ForeignKey("inspection.Inspection_ID"),
        nullable=False,
    )

    # -------------------------
    # DEFECT ATTRIBUTES
    # -------------------------

    # Code or abbreviation representing the primary type of defect, typically following a standard classification
    Defect_code = Column(String, nullable=False)

    # Additional code describing the nature  of the defect, complementing the main defect code.
    Characterization_code = Column(String, nullable=True)

    # Quantification or severity of the defect (e.g., size, percentage)
    Quantification = Column(String, nullable=True)

    # Distance from the starting manhole of the pipe to the location of the defect (m).
    Longitudinal_distance = Column(Float, nullable=True)

    # Clock position (from 0 to 12) indicating where the defect begins around the inner circumference of the pipe, using the pipe’s crown as the 12 o’clock reference.
    Circumferential_start = Column(Integer, nullable=True)

    # Clock position (from 0 to 12) indicating where the defect ends around the inner circumference of the pipe, using the same reference as Circumferential_start.
    Circumferential_end = Column(Integer, nullable=True)

    #The extent of the defects. Explain the start and finish of the defect (Example: S.01 and F.02)
    Continuous_defect=Column(String, nullable=True)

    # Free-text notes providing additional details or context about the defect.
    Comments = Column(String, nullable=True)

    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # Each defect belongs to a single inspection
    inspection = relationship(
        "Inspection",
        back_populates="defects",
    )

"""
# Section 3: Failures
==================

This section defines the Failure-related entities shown in the ERD.
"""

class Failure(Base):
    """
    Represents a failure event associated with a pipe and, when available,
    with a specific intervention. Each record describes the type of failure,
    when it occurred, its cause and the damage caused.
    """
    __tablename__ = "failure"

    # -------------------------
    # PRIMARY KEY
    # -------------------------
    # Unique identifier of the failure event
    Failure_ID = Column(Integer, primary_key=True, autoincrement=True)

    # -------------------------
    # RELATIONSHIPS (FOREIGN KEYS)
    # -------------------------

    # Identifier of the pipe where the failure occurred (FK to Pipe)
    Pipe_ID = Column(
        Integer,
        ForeignKey("pipe.Pipe_ID"),
        nullable=False,
    )

    # Identifier of the intervention associated with this failure (FK)
    # This can be nullable if not every failure is linked to a recorded intervention.
    Intervention_ID = Column(
        Integer,
        ForeignKey("intervention_history.Intervention_ID"),
        nullable=True,
    )

    # -------------------------
    # FAILURE ATTRIBUTES
    # -------------------------

    # General category or type of failure (e.g., flooding, blockage, collapse)
    Type_of_failure = Column(String, nullable=True)

    # Date when the failure occurred
    Date = Column(Date, nullable=True)

    #Provides the geographic or referential location of the failure, if available, which may include a physical address, geographic coordinates, or a reference along the pipe.
    Failure_location=Column(String, nullable=True)

    # Description of the main cause of the failure, if known. (e.g., roots, debris, structural collapse)
    Cause = Column(String, nullable=True)

    # Identifies the position where the underlying cause of the failure originated, which may differ from the location where the failure was observed.
    Cause_location = Column(String, nullable=True)

    # Description of the damage or impact resulting from the failure (e.g., flooding, service disruption, road damage).
    Damage_caused = Column(String, nullable=True)

    # Additional notes or comments about the failure event
    Comments = Column(String, nullable=True)


    # -------------------------
    # ORM RELATIONSHIPS
    # -------------------------

    # Each failure is associated with a single pipe (Pipe 1 -> N Failures)
    pipe = relationship(
        "Pipe",
        back_populates="failures",
    )

    # Each failure may be associated with one intervention history record
    # (Intervention_history 1 -> N Failures)
    intervention = relationship(
        "InterventionHistory",
        back_populates="failures",
    )

