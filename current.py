from pathlib import Path
from pprint import pprint
from textwrap import dedent, indent
import sqlite3 as sqlite


# Helper functions


def print_query(query, filepath=None):
    """Print the query/ies formatted, and write to file if filename
    provided"""
    if isinstance(query, list):
        query = "\n\n".join(query)
    if filepath is not None:
        filepath.write_text(query)
    query = indent(query, "\t")
    print(f"Executing:\n\n{query}")


# Constants

SQL_PATH = Path("sql/Exercism/")
SQL_PATH.mkdir(parents=True, exist_ok=True)


# Exersism SQLite path exercises


def gigasecond():
    """Exersism SQLite path exercise 4, Gigasecond:
    https://exercism.org/tracks/sqlite/exercises/gigasecond"""

    sql_path = SQL_PATH / "Gigasecond"
    sql_path.mkdir(parents=True, exist_ok=True)
    
    with sqlite.connect(":memory:") as con:
        query = dedent("""\
            CREATE TABLE gigasecond (moment TEXT, result TEXT);
            """)
        print_query(query, filepath=sql_path / "create_table.sql")        
        con.execute(query)
        query = dedent("""\
            INSERT INTO gigasecond (moment)
                VALUES
                    ('2011-04-25'),
                    ('1977-06-13'),
                    ('1959-07-19'),
                    ('2015-01-24T22:00:00'),
                    ('2015-01-24T23:59:59');
            """)
        print_query(query, filepath=sql_path / "insert_data.sql")
        con.execute(query)
        query = dedent("""\
            UPDATE gigasecond
            SET result = strftime('%Y-%m-%dT%H:%M:%S', moment, '1000000000 seconds');
            --SET result = strftime('%FT%T', moment, '1000000000 seconds');
            """)
        print_query(query, filepath=sql_path / "solution.sql")
        con.execute(query)
        query = "SELECT * FROM gigasecond;"
        res = con.execute(query)
        pprint(res.fetchall())


#gigasecond()


def difference_of_squares():
    """Exersism SQLite path exercise 3, Difference-of-Squares:
    https://exercism.org/tracks/sqlite/exercises/difference-of-squares"""

    sql_path = SQL_PATH / "Difference-of-Squares"
    sql_path.mkdir(parents=True, exist_ok=True)
    
    with sqlite.connect(":memory:") as con:
        query = dedent("""\
            CREATE TABLE "difference-of-squares"
                (number INT, property TEXT, result INT);
            """)
        print_query(query, filepath=sql_path / "create_table.sql")        
        con.execute(query)
        query = dedent("""\
            INSERT INTO "difference-of-squares" (number, property)
            VALUES
                (1, 'squareOfSum'),
                (5, 'squareOfSum'),
                (100, 'squareOfSum'),
                (1, 'sumOfSquares'),
                (5, 'sumOfSquares'),
                (100, 'sumOfSquares'),
                (1, 'differenceOfSquares'),
                (5, 'differenceOfSquares'),
                (100, 'differenceOfSquares');
            """)
        print_query(query, filepath=sql_path / "insert_data.sql")
        con.execute(query)
        query = dedent("""\
            UPDATE "difference-of-squares"
            SET result =
                CASE
                    WHEN property = 'squareOfSum' THEN
                        number * number * (number + 1) * (number + 1) / 4
                    WHEN property = 'sumOfSquares' THEN
                        number * (number + 1) * (2 * number + 1) / 6
                    ELSE
                        number * number * (number + 1) * (number + 1) / 4
                        - number * (number + 1) * (2 * number + 1) / 6
                END;
            """)
        print_query(query, filepath=sql_path / "solution.sql")
        con.execute(query)
        query = '''SELECT * FROM "difference-of-squares";'''
        res = con.execute(query)
        pprint(res.fetchall())


#difference_of_squares()


def darts():
    """Exersism SQLite path exercise 2, Darts:
    https://exercism.org/tracks/sqlite/exercises/darts"""

    sql_path = SQL_PATH / "Darts"
    sql_path.mkdir(parents=True, exist_ok=True)
    
    with sqlite.connect(":memory:") as con:
        query = dedent("CREATE TABLE darts (x REAL, y REAL, score INT);\n\n")
        print_query(query, filepath=sql_path / "create_table.sql")        
        con.execute(query)
        query = dedent("""\
             INSERT INTO darts (x, y)
                VALUES
                    (-9, 9),
                    (0, 10),
                    (-5, 0),
                    (0, -1),
                    (0, 0),
                    (-0.1, -0.1),
                    (0.7, 0.7),
                    (0.8, -0.8),
                    (-3.5, 3.5),
                    (-3.6, -3.6),
                    (-7.0, 7.0),
                    (7.1, -7.1),
                    (0.5, -4);
            """)
        print_query(query, filepath=sql_path / "insert_data.sql")
        con.execute(query)
        query = dedent("""\
            UPDATE darts
            SET score = CASE
                            WHEN dist > 100 THEN 0
                            WHEN dist > 25 THEN 1
                            WHEN dist > 1 THEN 5
                            ELSE 10
                        END
            FROM (SELECT x, y, (x * x + y * y) AS dist FROM darts) as dists
            WHERE darts.x = dists.x AND darts.y = dists.y;
            """)
        print_query(query, filepath=sql_path / "solution.sql")
        con.execute(query)
        query = "SELECT * FROM darts;"
        res = con.execute(query)
        pprint(res.fetchall())


#darts()
