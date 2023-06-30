import sqlite3

def sqlite():
    # 连接到SQLite数据库（如果不存在则会创建）
    conn = sqlite3.connect('example.db')

    # 创建一个游标对象
    cursor = conn.cursor()

    # 创建一个表格
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')

    # 插入数据
    cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('John Doe', 30))
    cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('Jane Smith', 25))

    # 提交事务
    conn.commit()

    # 查询数据
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # 关闭数据库连接
    conn.close()
