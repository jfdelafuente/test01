from typing import Union

from fastapi import FastAPI

from api.config import postgres_config
import psycopg2
import psycopg2.extras

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "How Cool": "Is This?"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/test_sql_query")
def test_sql_query():
    conn = None
    try:
        params = postgres_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql_stmt = f"SELECT * FROM test_user;"
        cur.execute(sql_stmt)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return {"results": results}
    except (Exception, psycopg2.DatabaseError) as error:
        if conn is not None:
            conn.close()
        return {"error": str(error)}
    finally:
        if conn is not None:
            conn.close()