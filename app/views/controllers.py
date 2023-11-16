"""
NAME:          views\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""

from flask import Blueprint, render_template, request
from app.database.controllers import Database

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = [r[0] for r in db_mod.get_distinct_pcts()]
    if request.method == 'POST':
        # if selecting PCT for table, update based on user choice
        form = request.form
        selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
    else:
        # pick a default PCT to show
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)

    # prepare data
    bar_data = generate_barchart_data()
    bar_values = bar_data[0]
    bar_labels = bar_data[1]
    title_data_items = generate_data_for_tiles()

    # calculate infection percentages
    infection_chart_data = generate_infection_barchart_data()

    chart_data = {
        'tile_data': title_data_items,
        'pct': {'data': bar_values, 'labels': bar_labels},
        'pct_list': pcts,
        'pct_data': selected_pct_data,
        'infection_chart_data': infection_chart_data
    }

    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html', **chart_data)

def generate_data_for_tiles():
    """Generate the data for the four home page titles."""
    return [db_mod.get_total_number_items(), db_mod.get_unique_items(), db_mod.get_average_cost()]

def generate_barchart_data():
    """Generate the data needed to populate the barchart."""
    data_values = db_mod.get_prescribed_items_per_pct()
    pct_codes = db_mod.get_distinct_pcts()

    # convert into lists and return
    data_values = [r[0] for r in data_values]
    pct_codes = [r[0] for r in pct_codes]
    return [data_values, pct_codes]

def generate_infection_barchart_data():
    # Calculate the percentage of each specific infection drug
    infection_sum=db_mod.get_items_sum("05%")
    antibacterial_per = format(round(db_mod.get_items_sum('0501%') / infection_sum, 4) * 100, '.2f')
    antifungal_per = format(round(db_mod.get_items_sum('0502%') / infection_sum, 4) * 100, '.2f')
    antiviral_per = format(round(db_mod.get_items_sum('0503%') / infection_sum, 4) * 100, '.2f')
    antiprotozoal_per = format(round(db_mod.get_items_sum('0504%') / infection_sum, 4) * 100, '.2f')
    antihelmintics_per = format(round(db_mod.get_items_sum('0505%') / infection_sum, 4) * 100, '.2f')

    result =  {'Antibacterial': antibacterial_per, 'Antifungal': antifungal_per, 'Antiviral': antiviral_per,
            'Antoprotozoal': antiprotozoal_per, 'Antihelmintics': antihelmintics_per}

    print(result)

    return result



