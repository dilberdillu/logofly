from sqlalchemy.orm import Session
from schemas.logo import CreateLogo
from db.models.logo import Logo

def create_new_logo(logo: CreateLogo, db: Session, creator_id: int = 1):
    logo = Logo(
        prompt=logo.prompt,
        image = logo.image,
        creator_id = creator_id
    )
    db.add(logo)
    db.commit()
    db.refresh(logo)
    return logo