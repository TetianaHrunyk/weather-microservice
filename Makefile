create_db:
	sqlite3 database.db -init schema.sql
	# then type in .quit
