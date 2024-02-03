# Volume Mount 지정
Rancher Desktop 에서 실행 시 볼륨 마운트가 되지 않아 컨테이너 실행과 동시에 종료되는 현상

```shell
# 볼륨을 생성합니다.
$ docker volume create mariadb_data

# 생성된 볼륨을 확인
$ docker volume inspect mariadb_data
[
    {
        "CreatedAt": "2022-05-09T05:26:48Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/mariadb_data/_data",
        "Name": "mariadb_data",
        "Options": {},
        "Scope": "local"
    }
]
```

Mountpoint 에 지정된 경로가 로컬 마운트 경로 입니다.
`docker-compose.yml` 파일에서 mariadb의 데이터 경로를 해당 경로로 수정합니다.

```yaml
    volumes:
#      - ./mariadb/data:/var/lib/mysql
      - /var/lib/docker/volumes/mariadb_data/_data:/var/lib/mysql
      - ./mariadb/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d
```

## 참고
Docker Desktop 을 사용하는 경우 `docker-compose.yml` 에 명시된 볼륨이 자동으로 생성됩니다.