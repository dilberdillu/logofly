from fastapi import APIRouter, HTTPException, Request, Depends, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.session import get_db
from typing import Optional
from db.models.user import User
from apis.v1.route_login import get_current_user
from jose import jwt, JWTError, ExpiredSignatureError
from core.config import settings
from db.repository.login import get_user_by_email


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def home(request: Request, alert: Optional[str] = None, db: Session = Depends(get_db)):
    # print(dir(request))
    token = request.cookies.get("access_token")
    if not token:
        # Redirect to login if token is missing
        return responses.RedirectResponse(url="/auth/login", status_code=status.HTTP_302_FOUND)
    token = token.replace("Bearer ", "")
    print(token)
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credential_exception
    except ExpiredSignatureError:
        return templates.TemplateResponse("/auth/login.html", {"request": request, "alert": alert})
    except JWTError as e:
        raise credential_exception

    user = get_user_by_email(email=email, db=db)
    if user is None:
        raise credential_exception
    
    context = {"request": request, "alert": alert, "user": user}
    return templates.TemplateResponse("logos/home.html", context=context)