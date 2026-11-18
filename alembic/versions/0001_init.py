def upgrade(op, table):
    op.execute(f"ALTER TABLE {table} ADD COLUMN x int")
