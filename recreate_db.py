from db_models import Base
import db

print("Dropping and creating tables")
Base.metadata.drop_all(db.engine)
Base.metadata.create_all(db.engine)
print("Tables created")
