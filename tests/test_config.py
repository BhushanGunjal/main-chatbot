from config.settings import settings
print("Import: SUCCESSFUL")



if settings.openai_api_key != "":
    print("API Key import: SUCCESSFUL")
else:
    print("API Key import: FAILURE")



if settings.chroma_db_path != "":
    print("CHROME DB path import: SUCCESSFUL: set as >",settings.chroma_db_path)
else:
    print("CHROME DB path import: FAILURE")
    


if settings.env != "NULL":
    print("ENV import: SUCCESSFUL: set as >",settings.env)
else:
    print("ENV import: FAILURE")