from fastapi import APIRouter, status
from app.api.deps import DBSession, CurrentUser
from app.models.note import NoteRead, NoteCreate, NoteUpdate
from app.services.note_services import NoteServices

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)



@router.get("/", response_model = list[NoteRead])
def list_notes(db: DBSession, user: CurrentUser):
    return NoteServices(db).list_visible(user.id)



@router.post("/", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, db: DBSession, user: CurrentUser):
    return NoteServices(db).create(user.id, payload)



@router.patch("/{note_id}", response_model=NoteRead)
def update_note(note_id: int, payload: NoteUpdate, db: DBSession, user: CurrentUser):
    return NoteServices(db).update(user.id, note_id, payload)



@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: DBSession, user: CurrentUser):
    NoteServices(db).delete(user.id, note_id)

    return None