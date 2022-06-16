# TUGAS-SOA-POINT-HARD
Department News Board

Service ini memakai Bahasa Pemrograman Python

Untuk menjalankan service nya menggunakan Nameko, RabbitMQ

Service ini Terhubung dengan Database menggunakan MySQL.

Untuk melakukan pengetesan API menggunakan Postman.

# Step by Step untuk melakukan pengetesan service ini
1. Import database yang sudah disediakan
2. Melakukan Run di Visual Studio Code di 2 terminal : nameko run service dan nameko run news_service
3. Buka Postman untuk test API

# Untuk mengakses Service
1. Register : 127.0.0.1:8000/register
2. Login    : 127.0.0.1:8000/login
3. Log Out  : 127.0.0.1:8000/logout

# Untuk Service Department News Board
1. Add News             : 127.0.0.1:8000/add
2. Edit News            : 127.0.0.1:8000/edit
3. Get All News         : 127.0.0.1:8000/getall
4. Get News by ID       : 127.0.0.1:8000/getbyid
5. Delete News          : 127.0.0.1:8000/delete
6. Download File by ID  : 127.0.0.1:8000/download
