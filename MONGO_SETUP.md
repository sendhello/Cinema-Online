Настройка кластера Mongo

Для начала настроим серверы конфигурации.
```commandline
docker exec -it mongocfg1 bash -c 'echo "rs.initiate({_id: \"mongors1conf\", configsvr: true, members: [{_id: 0, host: \"mongocfg1\"}, {_id: 1, host: \"mongocfg2\"}, {_id: 2, host: \"mongocfg3\"}]})" | mongosh'
```

Можно проверить статус, выполнив команду на первом сервере конфигурации.
```commandline
docker exec -it mongocfg1 bash -c 'echo "rs.status()" | mongosh'
```

Далее, соберём набор реплик первого шарда.
```commandline
docker exec -it mongors1n1 bash -c 'echo "rs.initiate({_id: \"mongors1\", members: [{_id: 0, host: \"mongors1n1\"}, {_id: 1, host: \"mongors1n2\"}, {_id: 2, host: \"mongors1n3\"}]})" | mongosh'
```

Теперь ноды шарда знают друг друга. Один из них стал первичным (primary), а два других — вторичными (secondary). Вы можете проверить статус реплик с помощью такой команды:
```commandline
docker exec -it mongors1n1 bash -c 'echo "rs.status()" | mongosh'
```

Наконец, познакомим шард с маршрутизаторами.
```commandline
docker exec -it mongos1 bash -c 'echo "sh.addShard(\"mongors1/mongors1n1\")" | mongosh'
```

Второй шард добавим по аналогии. Сначала инициализируем реплики.
```commandline
docker exec -it mongors2n1 bash -c 'echo "rs.initiate({_id: \"mongors2\", members: [{_id: 0, host: \"mongors2n1\"}, {_id: 1, host: \"mongors2n2\"}, {_id: 2, host: \"mongors2n3\"}]})" | mongosh'
```
Затем добавим их в кластер.
```commandline
docker exec -it mongos1 bash -c 'echo "sh.addShard(\"mongors2/mongors2n1\")" | mongosh'
```

Теперь маршрутизаторы-интерфейсы кластера для клиентов знают о существовании шардов. Можно проверить статус с помощью команды, запущенной на первом маршрутизаторе.
```commandline
docker exec -it mongos1 bash -c 'echo "sh.status()" | mongosh'
```

Теперь кластер полностью сконфигурирован, но у вас пока нет ни одной базы данных. Создадим тестовую БД.
```commandline
docker exec -it mongors1n1 bash -c 'echo "use someDb" | mongosh'
```
Включим шардирование.
```commandline
docker exec -it mongos1 bash -c 'echo "sh.enableSharding(\"someDb\")" | mongosh'
```

Теперь у вас есть база данных с подключённым шардированием в кластере MongoDB. Пришло время создать тестовую коллекцию.
```commandline
docker exec -it mongos1 bash -c 'echo "db.createCollection(\"someDb.someCollection\")" | mongosh'
```

Эта коллекция ещё не шардируется. Настроим шардирование по полю someField.
```commandline
docker exec -it mongos1 bash -c 'echo "sh.shardCollection(\"someDb.someCollection\", {\"someField\": \"hashed\"})" | mongosh'
```