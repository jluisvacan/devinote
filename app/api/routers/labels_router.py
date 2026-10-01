from fastapi import APIRouter, status
from app.api.deps import DBSession, CurrentUser
from app.models.label import LabelRead, Label, LabelCreate
from app.models.share import ShareRequest
from app.services.label_services import LabelServices
from app.services.share_services import ShareServices

router = APIRouter(
    prefix="/labels",
    tags=["Labels"]
)

@router.get("/", response_model=list[LabelRead], status_code=status.HTTP_200_OK)
def list_labels(db: DBSession, user: CurrentUser) -> list[Label]:
    return LabelServices(db).list(user.id)



@router.post("/", response_model=LabelRead, status_code=status.HTTP_201_CREATED)
def create_label(payload: LabelCreate, db: DBSession, user: CurrentUser):
    return LabelServices(db).create(user.id, payload)



@router.delete("/{label_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_label(label_id: int, db: DBSession, user: CurrentUser):
    LabelServices(db).delete(user.id, label_id)