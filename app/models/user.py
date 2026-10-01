from sqlmodel import SQLModel, Field

#creacion de tabla
class User(SQLModel, table=True):
    __tablename__ = "user"
    id: int = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: str = Field(default="")
    hashed_password: str
    active: bool = Field(default=True)


#validador
class UserCreate(SQLModel):
    email: str
    full_name: str = ""
    password: str


#validador
class UserRead(SQLModel):
    id: int
    email: str
    full_name: str
    model_config = {"from_attributes": True}
