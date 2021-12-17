
import sqlite3

with open("test.wav", "rb") as bin_wav:
    b = bin_wav.read()
print(b, type(b))

# with open("test_out.wav", "wb") as wav_out:
#     wav_out.write(b)

connection = sqlite3.connect("projectmusic.db")
cursor = connection.cursor()
query = f"""INSERT INTO fff (name_track, byts) VALUES ("song1", {b})"""
result = cursor.execute(query)
connection.commit()




