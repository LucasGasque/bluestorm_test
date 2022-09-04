from http import HTTPStatus
from traceback import print_exc
from fastapi.exceptions import HTTPException
from app.configs.password import get_password_hash
from app.exceptions.username_taken import UsernameTaken


from app.models.users import Users
from app.schemas.users import UserOut


async def create_user_controller(user, db):
    try:
        username_taken = db.query(Users).filter(Users.username == user.username).first()

        if username_taken:
            raise UsernameTaken

        hashed_password = get_password_hash(user.password)
        db_user = Users(username=user.username, password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return UserOut.from_orm(db_user)

    except UsernameTaken:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "Username already exists")

    except Exception:
        print_exc()
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, "Internal server error")
