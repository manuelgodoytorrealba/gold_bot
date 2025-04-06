#!/bin/bash

# Cargar variables desde .env
export $(grep -v '^#' /Users/home/Desktop/bot_oro/.env | xargs)

# Ejecutar script con el Python del entorno virtual
/Users/home/Desktop/bot_oro/venv/bin/python3 /Users/home/Desktop/bot_oro/bot_oro.py

# Confirmar ejecución en el log
echo "Cron ejecutó esto a $(date)" >> /Users/home/Desktop/bot_oro/logs/log_debug.txt
