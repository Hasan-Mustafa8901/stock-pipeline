from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection Config

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '@Hasan123',
    database = 'stockDB'
)

@app.route('/', methods=['GET'])
def index():
    cursor = db.cursor()

    # Get distinct tickers for dropdown
    cursor.execute('SELECT DISTINCT ticker FROM stocksdata;')
    tickers = [row[0] for row in cursor.fetchall()]


    # Get user selection from query params
    selected_ticker = request.args.get('ticker', tickers[0]) # Default to first ticker
    start_date = request.args.get('start_date','2020-01-01')
    end_date = request.args.get('end_date','2020-12-01')


    # Fetch filtered data
    query = """SELECT * 
            FROM stocksdata WHERE ticker = %s AND date BETWEEN %s and %s
            ORDER BY date ASC
            LIMIT 50;
    """
    cursor.execute(query,(selected_ticker,start_date,end_date))
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    # Extract chart data from 
    chart_dates = [row[0].strftime('%Y-%m-%d') for row in data] # row[0] = date
    chart_close = [row[4] for row in data] # row[4] = close price

    ## Summary Statistics Query
    stats_query = '''
            SELECT 
                AVG(open) as avg_open,
                AVG(close) as avg_close,
                AVG(daily_return) as avg_daily_return
            FROM stocksdata
            WHERE ticker= %s AND date BETWEEN %s AND %s;
    '''
    cursor.execute(stats_query, (selected_ticker,start_date,end_date))
    stats = cursor.fetchone()

    return render_template('home.html',
                           data=data,
                           columns=columns,
                           tickers=tickers,
                           selected = selected_ticker,
                           start_date=start_date,
                           end_date=end_date,
                           stats = stats,
                           chart_dates=chart_dates,
                           chart_close=chart_close)

if __name__ == '__main__':
    app.run(debug=True)