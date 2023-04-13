from errors import IncorrectUserInputError


def validate_user_choice(user_choice: str) -> None:
    if not user_choice.isdigit():
        raise IncorrectUserInputError("Choice must be digit.")

    if user_choice not in ("1", "6"):
        raise IncorrectUserInputError("Choice must be 1 or 6.")
