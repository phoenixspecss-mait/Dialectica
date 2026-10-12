from sqlmodel import create_engine

sqite_file_name = "dialaectia.db"
sqlite_url = f"sqlite:///{sqite_file_name}"

engine = create_engine(sqlite_url,echo=True)