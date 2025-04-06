#!/bin/bash

echo "🚀 Cron ejecutó run.sh a $(date)" >> /Users/home/proyectos/bot_oro/logs/log_debug.txt

# Activar entorno virtual
source /Users/home/proyectos/bot_oro/venv/bin/activate

# Exportar variables del .env
set -a
source /Users/home/proyectos/bot_oro/.env
set +a


# Ejecutar script principal
/Users/home/proyectos/bot_oro/venv/bin/python /Users/home/proyectos/bot_oro/bot_oro.py

# Registrar ejecución
echo "✅ Script ejecutado a $(date)" >> /Users/home/proyectos/bot_oro/logs/log_debug.txt
env >> /Users/home/proyectos/bot_oro/logs/log_debug.txt
