ARG NGINX_VERSION=latest
FROM nginx:${NGINX_VERSION}

# SSL 인증서와 개인 키 복사
# SSL 인증서는 이 예제에서는 자체 서명된 인증서를 사용하지만,
# 실제 배포에서는 신뢰할 수 있는 CA에서 발급받은 인증서를 사용해야 합니다.
#COPY ssl/myfastapi.crt /etc/ssl/certs/
#COPY ssl/myfastapi.key /etc/ssl/private/

# Nginx 설정 파일 복사
COPY nginx.conf /etc/nginx/conf.d/default.conf

#EXPOSE 80 443
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]
