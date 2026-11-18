def test_q(db, name):
    db.execute(f"SELECT * FROM t WHERE n = '{name}'")
