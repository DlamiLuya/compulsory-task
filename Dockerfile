FROM nginx
COPY . /usr/share/nginx/html
WORKDIR /food
RUN pip install -r requirements.txt
