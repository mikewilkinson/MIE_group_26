"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
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

    def get_antibiotics_prescriptions_by_practice(self, selected_pct):
        """Query the total quantity of antibiotics for each GP practice in the selected PCT."""
        antibiotics_prescriptions = db.session.query(
            PrescribingData.practice,
            func.sum(PrescribingData.quantity).label('total_quantity')
        ).filter(
            PrescribingData.PCT == selected_pct,
            PrescribingData.BNF_code.startswith('05')
        ).group_by(PrescribingData.practice).all()

        return antibiotics_prescriptions
    def max_quantity_percentage(self):
        """Return the top precribed item."""
        # 求和
        column_sum = db.session.query(func.sum(PrescribingData.quantity)).scalar()
        # 最大值
        max_value = db.session.query(func.max(PrescribingData.quantity)).scalar()
        #top prescribed item = 
        # 计算百分比
        max_value_percentage = round((max_value / column_sum) * 100,2)
        row_with_max_quantity = db.session.query(PrescribingData).filter(PrescribingData.quantity == max_value).one()
        top_prescribed_item = row_with_max_quantity.BNF_name
        return max_value_percentage,top_prescribed_item
    
    def agerage_cost(self):
        return round(float(db.session.query(func.avg(PrescribingData.ACT_cost)).first()[0]), 2)

    def number_of_unique_items(self):
        return int(db.session.query(func.count(PrescribingData.BNF_code.distinct())).first()[0])


    def get_items_sum(self, items):
        """Return sum of infection treatments with BNF codes 05"""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')) \
            .filter(PrescribingData.BNF_code.like(items)) \
            .first()[0]

    def search_drug(self, search_query):
        """
        Search for drugs based on BNF code or drug name.
        """
        search_result = db.session.query(
            PrescribingData.BNF_code,
            PrescribingData.BNF_name,
            func.count(PrescribingData.practice).label('num_practices'),
            func.sum(PrescribingData.items).label('item_sum'),
            (func.avg(PrescribingData.ACT_cost)/func.count(PrescribingData.items)).label('avg_cost')
        ).filter(
            db.or_(
                PrescribingData.BNF_code.like(f'%{search_query}%'),
                PrescribingData.BNF_name.like(f'%{search_query}%')
            )
        ).group_by(
            PrescribingData.BNF_code,
            PrescribingData.BNF_name
        ).all()

        return search_result

