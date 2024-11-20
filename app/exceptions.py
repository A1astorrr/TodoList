from fastapi import HTTPException, status

TodoByIdNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Запись по данному id не найдена"
)

TodoNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Ошибка в создание записи",
)

TodoNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Запись не обновлена.",
)

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Запись с таким id не найден"
)

TodoCreated = HTTPException(
    status_code=status.HTTP_201_CREATED, detail="Запись создана"
)

TodoUpdated = HTTPException(
    status_code=status.HTTP_202_ACCEPTED, detail="Запись редактирована"
)

TodoDeleted = HTTPException(status_code=status.HTTP_200_OK, detail="Запись удалена")
