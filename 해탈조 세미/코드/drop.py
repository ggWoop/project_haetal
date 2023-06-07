import matplotlib.pyplot as plt

def fetch_data():
    change_sql = """
    SELECT 
        date, tourism, business, official_affairs, studying, others
    FROM 
        enter_korea 
    WHERE 
        nation = 'china' 
        AND 
        date IN ('2019-12', '2020-1', '2020-2', '2020-3', '2020-4')
    """

    with conn.cursor() as cursor:
        cursor.execute(change_sql)
        result = cursor.fetchall()

    return result

def plot_data(result):
    dates = [row[0] for row in result]
    categories = ['tourism', 'business', 'official_affairs', 'studying', 'others']
    data = [[int(row[i]) for row in result] for i in range(1, 6)]

    for category, values in zip(categories, data):
        plt.plot(dates, values, marker='o', linestyle='-', label=category.capitalize())

    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Visitors by Category from Dec 2019 to Apr 2020')

    plt.xticks(rotation=45, ha='right')
    plt.legend()
	#plt.ylim(0, 100000) 
    plt.show()

# 데이터 가져오기
result = fetch_data()

# 그래프 그리기
plot_data(result)