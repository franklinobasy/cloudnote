import uvicorn
from fastapi import FastAPI
from server1 import session
from server1.models import User, Note

app = FastAPI()

@app.get("/")
def root():
    return {"version": "1.01"}

@app.get('/api/cloudnote/notes')
async def fetch_notes():
    notes = session.query(Note).all()
    output = dict()
    for note in notes:
        output[note.id] = {
            "title" : note.name,
            "author_id": note.author_id,
            "date" : str(note.date)
        }
    return output


if __name__ == "__main__":
    uvicorn.run("main:app")