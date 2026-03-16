# Wake-up Light – TODO

## Infraestructura del proyecto

- [x] Crear logica de configuración `config.json` si no existe
- [x] Guardar variables sensibles (WiFi, tokens API)

---

## Conectividad

### Módulo WiFi

- [ ] Crear módulo `wifi.py`
- [ ] Implementar función de conexión
- [ ] Implementar reconexión automática
- [ ] Activar Access Point si falla conexión
- [ ] Crear interfaz mínima de configuración

Funciones esperadas:

- connect()
- start_access_point()
- scan_networks()
- save_credentials()

---

## Tiempo

### Sincronización de hora

- [ ] Crear `time_manager.py`
- [ ] Obtener hora desde NTP
- [ ] Rutina no bloqueante de actualización
- [ ] Manejo de zona horaria

Funciones:

- sync_time()
- get_local_time()
- periodic_update()

---

## Datos geográficos

### Ubicación aproximada

- [ ] Crear `geo_manager.py`
- [ ] Obtener ubicación mediante API

Funciones:

- get_location()

Opciones de API:
- ip-api
- ipinfo
- ipstack

---

## Astronomía

### Amanecer y atardecer

- [ ] Crear `sun_manager.py`
- [ ] Obtener hora de sunrise/sunset mediante API

Funciones:

- get_sun_times(lat, lon)

Opciones:
- sunrise-sunset.org
- NOAA API

---

## Control de iluminación

### PWM dimming

- [ ] Crear `light_controller.py`
- [ ] Inicializar PWM
- [ ] Implementar función de brillo
- [ ] Implementar transición (sunrise / sunset)

Funciones:

- set_brightness()
- start_sunrise()
- start_sunset()

Curvas posibles:
- gamma correction
- smoothstep
- sigmoid

---

## Sistema

### Logging

- [ ] Crear `logger.py`
- [ ] Log a consola
- [ ] Log a archivo (opcional)

---

### Tests

- [x] Crear carpeta `tests/`
- [ ] Tests de:
    - curvas de dimming
    - parsing de APIs
    - reconexión WiFi

---

## Mejoras futuras

- [ ] Interfaz web local
- [ ] Control desde app
- [ ] Configuración de horarios
- [ ] OTA updates