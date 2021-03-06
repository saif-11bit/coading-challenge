from sqlalchemy import create_engine
import sys
import pathlib
sys.path.extend([str(pathlib.Path(__file__).parent.parent.absolute())])
from models.gender_enrolled import GenderEnrolled, GenderEnum
from models.grade_enrolled import GradeEnrolled, GradeEnum
from models.race_enrolled import RaceEnrolled, RaceEnum
from models.category import Category
from models.school import School
from models.total_enrolled import TotalEnrolled
from models.chart import ChartEnrolled
import pandas as pd
from uuid import uuid4
from dotenv import load_dotenv
import os
import math

load_dotenv(verbose=True)

DB_URI=os.environ["DB_URI"]

engine = create_engine(DB_URI)


'''
Find category id by category_name
'''
def find_category_id_by_name(_name):
    with engine.begin() as connection:
        query = connection.execute(Category.select().where(Category.columns.category_name == _name))
        category = query.fetchone()
        return category['id']
   
    
'''
Find school id by dbn
'''
def find_school_id_by_dbn(_dbn):
    with engine.begin() as connection:
        query = connection.execute(School.select().where(School.columns.DBN == _dbn))
        school = query.fetchone()
        return school['id']


'''
Transfer Category data from csv to DB
'''
def transfer_category_data():
    with engine.begin() as connection:
        filename = 'app/csv_data/category_data.csv'
        categories = pd.read_csv(filename)
        for categ in categories.itertuples(index=False):
            with engine.begin() as connection:
                id = uuid4()
                connection.execute(Category.insert(), {"id": str(id), "category_name":categ})
                
                
'''
Transfer School data from csv to DB
'''
def transfer_school_data():
    with engine.begin() as connection:
        filename = 'app/csv_data/schools_data.csv'
        schools = pd.read_csv(filename)
        for dbn, schl_n in schools.itertuples(index=False):
            with engine.begin() as connection:
                id = uuid4()
                connection.execute(School.insert(), {"id": str(id), "DBN": dbn, "school_name":schl_n})


'''
Transfer Total Enrolled data from csv to DB
'''
def transfer_total_enrolled_data():
    with engine.begin() as connection:
        filename = 'app/csv_data/total_enrolled_data.csv'
        total_enrolled = pd.read_csv(filename)
        for dbn, cat, ttl in total_enrolled.itertuples(index=False):
            school = find_school_id_by_dbn(dbn)
            category = find_category_id_by_name(cat)
            ttl_enrolled = ttl
            with engine.begin() as connection:
                id = uuid4()
                connection.execute(TotalEnrolled.insert(),{"id":str(id), "category_id":category,"school_id":school, "count":ttl_enrolled if isinstance(ttl_enrolled, float) and math.isnan(float(ttl_enrolled)) == False else None})


'''
Transfer Genders Enrolled data from csv to DB
'''
def transfer_gender_enrolled_data():
    with engine.begin() as connection:
        filename = 'app/csv_data/gender_enrolled_data.csv'
        gender_enrolled = pd.read_csv(filename)
        for dbn, cat, female_c, female_per,male_c, male_per in gender_enrolled.itertuples(index=False):
            school = find_school_id_by_dbn(dbn)
            category = find_category_id_by_name(cat)
            female_c = female_c if female_c.isnumeric() else None
            female_per = str(female_per)
            male_c = male_c if male_c.isnumeric() else None
            male_per = str(male_per)
            with engine.begin() as connection:
                for gender in GenderEnum:
                        connection.execute(GenderEnrolled.insert(),{"id":str(uuid4()), "category_id":category,"school_id":school, "gender":gender,"percent":male_per if gender==GenderEnum.Male else female_per,"count":male_c if gender==GenderEnum.Male else female_c})


'''
Transfer Grade Enrolled data from csv to DB
'''
def transfer_grade_enrolled_data():
    with engine.begin() as connection:
        filename = 'app/csv_data/grade_enrolled_data.csv'
        grade_enrolled = pd.read_csv(filename)
        for dbn, cat, grade_k, grade_1, grade_2 ,grade_3, grade_4, grade_5 in grade_enrolled.itertuples(index=False):
            school = find_school_id_by_dbn(dbn)
            category = find_category_id_by_name(cat)
            
            with engine.begin() as connection:
                for grade in GradeEnum:
                    if grade == GradeEnum.Grade_K:
                        grade_c = grade_k
                    elif grade == GradeEnum.Grade_1:
                        grade_c = grade_1
                    elif grade == GradeEnum.Grade_2:
                        grade_c = grade_2
                    elif grade == GradeEnum.Grade_3:
                        grade_c = grade_3
                    elif grade == GradeEnum.Grade_4:
                        grade_c = grade_4
                    elif grade == GradeEnum.Grade_5:
                        grade_c = grade_5
                    connection.execute(GradeEnrolled.insert(),{"id":str(uuid4()), "category_id":category,"school_id":school, "grade": grade, "count": grade_c if grade_c.isnumeric() else None})



'''
Transfer Race Enrolled data from csv to DB
'''
def transfer_race_enrolled_data():
    with engine.begin() as connection:
        filename = 'app/csv_data/race_enrolled_data.csv'
        grade_enrolled = pd.read_csv(filename)
        for dbn, cat, asian_c, asian_per, black_c, black_per, hispanic_c, hispanic_per  in grade_enrolled.itertuples(index=False):
            school = find_school_id_by_dbn(dbn)
            category = find_category_id_by_name(cat)
            
            with engine.begin() as connection:
                for race in RaceEnum:
                    if race == RaceEnum.Asian:
                        race_c = asian_c if asian_c.isnumeric() else None
                        race_per = asian_per
                    elif race == RaceEnum.Black:
                        race_c = black_c if black_c.isnumeric() else None
                        race_per = black_per
                    elif race == RaceEnum.Hispanic:
                        race_c = hispanic_c if hispanic_c.isnumeric() else None
                        race_per = hispanic_per
                    connection.execute(RaceEnrolled.insert(),{"id":str(uuid4()), "category_id":category,"school_id":school, "race": race, "percent":race_per,"count": race_c})



'''
Insert Chart Data in Chart DB
'''
def add_chart_data(chart_uuid, chart_data, enroll_type):
    with engine.begin() as connection:
        connection.execute(ChartEnrolled.insert(),{"id":str(chart_uuid), "enrollment_type":enroll_type,"mean_data":chart_data})
