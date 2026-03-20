from src.database import SongDatabase
from src.recognize import recognize, record_and_recognize
from src.utils import load_audio

# Index songs
db = SongDatabase()
db.index_directory("songs/")

while True:
    input("press enter to start recognizing...")
    best_name, best_score, all_scores=record_and_recognize(db)
    
print(f"Match: {name} (score: {score})")
print(f"Hash table stats: {db.table.stats()}")