import psycopg2


def dangerous_query(user_input, conn_params):
    try:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                # Построение SQL-запроса с использованием строки, введенной пользователем напрямую
                query = f"SELECT id, name, status FROM obvious.persons WHERE name = '{user_input}'"

                # Выполнение запроса
                cur.execute(query)
                results = cur.fetchall()

                if results:
                    for result in results:
                        print(f"ID: {result[0]}, Name: {result[1]}, Status: {result[2]}")
                else:
                    print("No results found.")

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()


# Пример вызова функции с пользовательским вводом, который может содержать SQL-инъекцию
# Например, ввод: 'zn' OR '1'='1
dangerous_query("zn' OR '1'='1")
conn_params = {
    "dbname": "laba6",
    "user": "",
    "password": "",
    "host": "",
    "port": "",
}
