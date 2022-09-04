from datetime import timedelta
from http import HTTPStatus
from traceback import print_exc
from fastapi.exceptions import HTTPException

from app.configs.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from app.exceptions.unauthorized import Unauthorized
from app.services.users import authenticate_user


async def login_user_controller(form_data, db):
    try:
        user = authenticate_user(db, form_data.username, form_data.password)

        if not user:
            raise Unauthorized

        acces_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        acces_token = create_access_token(
            data={"sub": user.username}, expires_delta=acces_token_expires
        )

        return {"access_token": acces_token, "token_type": "bearer"}

    except Unauthorized:
        raise HTTPException(
            HTTPStatus.UNAUTHORIZED, detail="Incorrect username or password"
        )

    except Exception:
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, "Internal server error")
