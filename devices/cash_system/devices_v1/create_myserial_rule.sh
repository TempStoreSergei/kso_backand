#!/bin/sh

RULE_FILE="/etc/udev/rules.d/99-myserial.rules"

# Создаем правило
echo 'SUBSYSTEM=="tty", KERNEL=="ttyS*", ATTRS{id}=="PNP0501", SYMLINK+="myserial"' | sudo tee $RULE_FILE > /dev/null

# Обновляем правила
sudo udevadm control --reload-rules
sudo udevadm trigger

# Проверяем результат
ls -l /dev/myserial 2>/dev/null || echo "⚠️ Симлинк /dev/myserial пока не найден. Попробуйте переподключить устройство."
