1. Create virtualenv for local project
    1.1 mkvirtualenv "env name"
    1.2 add workon for virtualenvwrapper
    1.3 workon "env name"
2. Install Django and packages
    2.1 pip install requirements.txt
    2.2 install postgresql
3. Install Redis and RabbitMQ
    3.1 brew install rabbitmq
    3.2 brew services start rabbitmq(
    or background mode
    CONF_ENV_FILE="/opt/homebrew/etc/rabbitmq/rabbitmq-env.conf" /opt/homebrew/opt/rabbitmq/sbin/rabbitmq-server
)
    3.3 brew install redis
    3.4 brew services start redis
    3.5 redis-cli (connect to redis)
4. Run app
    4.1 python manage.py makemigrations
    4.2 python manage.py migrate
    4.3 run redis and rabbitmq
    4.4 python manage.py runserver (check on localhost)
