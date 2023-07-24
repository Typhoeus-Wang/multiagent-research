dev:
	uvicorn db_app.main:app --reload --host 0.0.0.0

prod:
	uvicorn db_app.main:app --host 0.0.0.0