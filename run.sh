#!/bin/bash

# Registrar que el script fue ejecutado por cron o manualmente
echo "🚀 run.sh ejecutado a $(date)" >> /Users/home/proyectos/bot_oro/logs/log_debug.txt

# Activar entorno virtual
source /Users/home/proyectos/bot_oro/venv/bin/activate

# Ejecutar script Python
python3 /Users/home/proyectos/bot_oro/bot_oro.py

# Registrar fin de ejecución
echo "✅ Script finalizado a $(date)" >> /Users/home/proyectos/bot_oro/logs/log_debug.txt
