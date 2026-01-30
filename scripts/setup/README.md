./scripts/setup/init_project.sh              # Повний setup
./scripts/setup/init_project.sh --quick      # Швидкий режим (менше даних)
./scripts/setup/init_project.sh --skip-build # Без білда Docker
./scripts/setup/init_project.sh --skip-data  # Без генерації даних
./scripts/setup/init_project.sh --help       # Допомога
```

✅ **Кольоровий output:**
- 🔵 Info messages
- 🟢 Success messages
- 🟡 Step indicators
- 🔴 Error messages

✅ **Розумні перевірки:**
- Чи Docker running
- Чи Python 3.10+
- Чи достатньо disk space (10GB+)
- Чи достатньо RAM (8GB+)

✅ **Graceful failures:**
- Якщо якийсь крок падає - зрозумілі повідомлення
- Пропозиції як пофіксити
- Exit codes для automation

✅ **Progress tracking:**
- Dots для довгих операцій
- Timestamps для кожного кроку
- Clear summary в кінці

✅ **Service health checks:**
- Автоматична перевірка доступності
- Retry logic з timeout
- Clear status для кожного сервісу

## 📋 Приклад виводу:
```
==============================================================================
  E-commerce Agent System - Project Initialization
==============================================================================
Course: End-to-End MLOps, LLMOps & AgenticOps
Module: 01 - Foundations & Project Setup

[10:30:15] [1/9] Checking prerequisites...
✓ docker found: /usr/local/bin/docker
  Version: Docker version 24.0.6
✓ Docker daemon is running
✓ Docker Compose found (Plugin): v2.21.0
✓ python3 found: /usr/bin/python3
  Version: Python 3.10.12
✓ git found: /usr/bin/git
✓ Sufficient disk space available: 45GB
✓ All prerequisites met!

[10:30:22] [2/9] Setting up environment...
✓ Created necessary directories
✓ Created docker/.env from template
✓ Virtual environment created
✓ Python dependencies installed

...

==============================================================================
  ✓ Setup Complete!
==============================================================================

All services are now running!

Service URLs:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ML Service:      http://localhost:8001     (Health: /health)
  RAG Service:     http://localhost:8002     (Health: /health)
  Agent Service:   http://localhost:8003     (Health: /health)
  MLflow UI:       http://localhost:5000
  Grafana:         http://localhost:3000     (admin/admin)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Happy Learning! 🚀