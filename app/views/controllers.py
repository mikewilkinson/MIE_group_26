"""
NAME:          views\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""
from flask import jsonify

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

    selected_pct_data = []
    search_results = []
    search_query = ''
    error_message = None  # Initialize an error message variable
    if request.method == 'POST':
        form = request.form
        if 'pct-option' in form and form['pct-option']:
            # if selecting PCT for table, update based on user choice
            selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
        elif 'search' in form and form['search']:
            # if performing a search, update based on user input
            search_query = form['search']
            search_results = db_mod.search_drug(search_query)
            if not search_results:
                error_message = "No results found for your search."
            # else branch is not needed here because the 'pct-option' and 'search' fields are mutually exclusive

        if not selected_pct_data and not request.method == 'POST':
            # pick a default PCT to show on initial GET request or if no POST data is provided
            selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)

     # prepare data
    bar_data = generate_barchart_data()
    bar_values = bar_data[0]
    bar_labels = bar_data[1]
    title_data_items = generate_data_for_tiles()
    max_value_percentage,top_prescribed_item = db_mod.max_quantity_percentage()
    agerage_cost = db_mod.agerage_cost()
    number_of_unique_items = db_mod.number_of_unique_items()
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
    return render_template('dashboard/index.html', search_results=search_results, search_query=search_query, error_message=error_message,
                           tile_data=title_data_items,
                           pct={'data': bar_values, 'labels': bar_labels},
                           pct_list=pcts, pct_data=selected_pct_data,max_value_percentage = max_value_percentage,
                           top_prescribed_item=top_prescribed_item,agerage_cost=agerage_cost,number_of_unique_items=number_of_unique_items)

def generate_data_for_tiles():
    """Generate the data for the four home page titles."""
    return [db_mod.get_total_number_items()]

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

@views.route('/get_antibiotics_data', methods=['POST'])
def get_antibiotics_data():
    selected_pct = request.json.get('selected_pct')
    antibiotics_data = db_mod.get_antibiotics_prescriptions_by_practice(selected_pct)
    # JSON
    data = [{'practice': record.practice, 'total_quantity': record.total_quantity} for record in antibiotics_data]
    return jsonify(data)