import matplotlib.pyplot as plt

def fetch_data():
    covid_sql = """
    SELECT 
    date, total
    from
    covid limit 106;
    """

    with conn.cursor() as cursor:
        cursor.execute(covid_sql)
        result = cursor.fetchall()

    return result

def plot_data(result):
    dates = [row[0] for row in result]
    totals = [row[1] for row in result]

    plt.plot(dates, totals, linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Total Confirmed Cases')
    plt.title('COVID-19 Confirmed Cases over Time')
    plt.xticks([])

    plt.show()
    
    
result = fetch_data()

plot_data(result)