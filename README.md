# FASTAPI BE TEMPLATE

## Công nghệ sử dụng
1. Fastapi: https://fastapi.tiangolo.com/
2. fastapi-crudrouter: https://fastapi-crudrouter.awtkns.com/
3. SQLModel: https://sqlmodel.tiangolo.com/
4. SQLAchemy: https://www.sqlalchemy.org/

## Cài đặt môi trường:

- Python: v3.10 (3.10.6)
- Sử dụng Pipenv để tạo Virtual env

```bash
# Cài đặt pipenv
pip install pipenv

```

## Sử dụng template:

1. Clone template về
2. CD vào thư mục gốc của template, ngang hàng với Pipfile
3. Tạo virtualenv bằng lệnh
```bash
# Tạo virtualenv
pipenv install

# kích hoạt (active) virtualenv
pipenv shell
```
4. Sửa biến môi trường trước khi chạy project
> Copy file .env.example thành file .env và sửa các thông tin DB connection

5. Chạy project:
```bash
# Chạy bằng lệnh
pipenv run bash ./scripts/start-dev.sh
```
Sau khi chạy xong, API sẽ listen tại: http://localhost:8000

Truy cập địa chỉ: http://localhost:8000/docs để xem documents

Trên documents có thể xem thông tin mô tả models & và test thử api

> Lưu ý phải chạy bằng pipenv để có thể load các biến môi trường từ file .env vào Config tự động


## Custom route khi logic không chỉ đơn giản là CRUD

fastapi-crudrouter sẽ tự động sinh ra các API handler cho các nghiệp vụ CRUD cơ bản màn chúng ta chỉ cần khởi tạo bằng việc truyền vào định nghĩa của Model giúp giảm bớt việc phải code lại những thứ đơng giản

Các route mặc định sẽ được tạo ra bởi fastapi-crudrouter:

- /	GET -> Get all the resources
- /	POST -> Create a new resource
- /	DELETE -> Delete all the resources
- /{item_id}	GET -> Get an existing resource matching the given item_id
- /{item_id}	PUT -> Update an existing resource matching the given item_id
- /{item_id}	DELETE -> Delete an existing resource matching the given item_id

tuy nhiên trên thực tế có những nghiệp vụ phức taph hơn thì ta có thể custom - ghi đè lại handler function tuỳ ý. tham khảo tài liệu bên dưới




- https://fastapi-crudrouter.awtkns.com/routing