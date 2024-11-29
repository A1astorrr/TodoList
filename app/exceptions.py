from fastapi import HTTPException, status

TodoByIdNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
)

TodoNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Ошибка в создание записи",
)

TodoNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Запись не обновлена",
)

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Запись  не найден"
)

