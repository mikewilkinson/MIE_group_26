"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func,distinct
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()

    def max_quantity_percentage(self):
        """Return the average ACT cost."""
        # 求和
        column_sum = db.session.query(func.sum(PrescribingData.quantity)).scalar()
        # 最大值
        max_value = db.session.query(func.max(PrescribingData.quantity)).scalar()
        #top prescribed item = 
        # 计算百分比
        max_value_percentage = round((max_value / column_sum) * 100,2) if column_sum else 0
        row_with_max_quantity = db.session.query(PrescribingData).filter(PrescribingData.quantity == max_value).first()
        top_prescribed_item = row_with_max_quantity.BNF_name
        return max_value_percentage,top_prescribed_item
    
    def agerage_cost(self):
        return round(float(db.session.query(func.avg(PrescribingData.ACT_cost)).first()[0]), 2)

    def number_of_unique_items(self):
        return int(db.session.query(func.count(PrescribingData.BNF_code.distinct())).first()[0])
