from fastapi import FastAPI
from pydantic import BaseModel
from CRUD.Add import router as add_router
from CRUD.Update import router as update_router
from CRUD.Delete import router as delete_router
from CRUD.Get import router as get_router
from access.dependencies import get_user_role

app = FastAPI()

class LoginRequest(BaseModel):
    name: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    result = get_user_role(request.name, request.password)
    role = result["role"]
    user = result["user"]
    
    response = {"message": f"Welcome {role.capitalize()} {user.name}", "role": role, "id": user.id}
    if role == "student":
        response["class_id"] = user.class_id
    return response

app.include_router(add_router, prefix="/crud", tags=["Add"])
app.include_router(update_router, prefix="/crud", tags=["Update"])
app.include_router(delete_router, prefix="/crud", tags=["Delete"])
app.include_router(get_router, prefix="/crud", tags=["Get"])


