# Nginx

## SSL 인증서 적용하기
```shell
$ cd nginx/ssl
$ brew install mkcert
$ mkcert -install -key-file key.pem -cert-file cert.pem "*.first-your-domain.com" "*.second-your-domain.com"
```