# LEARNING_LOG — путь к Junior DevOps

Цель: Junior DevOps. График: 3–4 часа в день, 5 дней в неделю.
Окружение: Ubuntu Server 26.04 (ARM64) в UTM на MacBook M1, доступ с Windows через Tailscale, VS Code Remote-SSH.

## Этапы

### Фаза 1. Linux и сети — пройдена, идёт повторение
- [x] Файловая система, права (`chmod`/`chown`), cron
- [x] Сеть: `ping`, `curl`, `ss`, `ufw`, `tcpdump`, TLS/openssl
- [x] SSH-ключи и защита SSH, `journalctl`, переменные окружения, `vim`
- [x] OverTheWire Bandit 0–15
- [ ] Повторение, блок 2: процессы и systemd (в т.ч. `health_check.py` как сервис с таймером)
- [ ] Повторение остальных блоков (сети, пользователи и права, логи)

### Фаза 2. Python, Bash, Git — почти закрыта
- [x] Bash: функции, циклы, `set -euo pipefail`, `trap`
- [x] `backup.sh`, `log_report.sh`
- [x] Python: `argparse`, `requests`, `json`, `try/except`, `health_check.py`
- [x] Git: ветки, rebase, cherry-pick, GitFlow, хуки, `.gitignore`, Pull Request, `fetch --prune`
- [x] Скрипт аудита сервера (Bash): сбор сведений о системе, диске, памяти, CPU и состоянии служб; предупреждение при заполнении диска выше порога и неактивных службах; итоговый код завершения 0/1
- [ ] Бэкап на Python с удалением архивов старше 7 дней
- [ ] Добавить `log_report.sh` в репозиторий `devops-scripts`

### Фаза 3. Docker — частично (около 55–60%)
- [x] Контейнеры, образы, Dockerfile, compose, bind mount, `.dockerignore`, Docker Hub
- [ ] Установить Docker на новую VM (ARM64)
- [ ] Докеризация Pet Manager: Dockerfile, multi-stage
- [ ] Compose с PostgreSQL 16, переменные `SPRING_DATASOURCE_*`, healthcheck, named volume
- [ ] Запуск не от root, trivy, публикация в `ghcr.io`

### Фаза 4. CI/CD и облако — начата (около 10%)
- [x] Первый файл GitHub Actions (не проверен)
- [ ] Остальное

### Фаза 5. Kubernetes и IaC — впереди
- [ ] Всё

## Ближайший план
1. Бэкап на Python с удалением архивов старше 7 дней
2. Фаза 1, блок 2: процессы и systemd
3. Докеризация Pet Manager

## Дневник

### 2026-11-16
- Переезд VM на MacBook завершён (UTM, Tailscale), восстановлены файлы и SSH-ключ GitHub.
- Закрыт Git-цикл: ветка `feature/timeout` → PR → merge → удаление ветки.
- `health_check.py` теперь поддерживает необязательное поле `timeout` в `sites.json` (по умолчанию 5 секунд).
- Написан Bash-скрипт аудита сервера: shebang, строгий режим (`set -Eeuo pipefail`), переменные и подстановка команд, `df`/`free`/`uptime`/`nproc`/`systemctl`, массивы и цикл `for`, условия `if`, арифметические сравнения, `awk`, форматирование через `printf` и коды завершения.
- Скрипт сообщает hostname, время работы, использование диска и памяти, число CPU-ядер и load average, проверяет службы `ssh` и `cron`; порог диска вынесен в переменную, предупреждения считаются, итог возвращает код `0` при успехе и `1` при предупреждениях.
- Повторены команды для получения справки (`--help`, `man`) и проверка кода завершения через `$?`.

<!-- Шаблон на каждый день:
### ГГГГ-ММ-ДД
- Что сделал:
- Что было сложно:
- Что дальше:
-->
