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

TodoCreated = HTTPException(
    status_code=status.HTTP_201_CREATED, detail="Запись создана"
)

TodoUpdated = HTTPException(
    status_code=status.HTTP_202_ACCEPTED, detail="Запись обновлена"
)

TodoDeleted = HTTPException(status_code=status.HTTP_200_OK, detail="Запись удалена")
