FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=1
ENV MYSQL_DATABASE=my_database
ENV MYSQL_USER=test_user
ENV MYSQL_PASSWORD=1

EXPOSE 3306

CMD ["mysqld"]