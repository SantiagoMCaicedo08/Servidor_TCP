# Servidor TCP con Thread Pool – Pruebas de Rendimiento usando JMeter

Este proyecto consiste en la implementación de un **servidor TCP en Python** capaz de manejar múltiples clientes de forma concurrente mediante el uso de un **Thread Pool**. El objetivo principal es analizar el comportamiento del servidor bajo carga, evaluando concurrencia, tiempos de respuesta y persistencia, utilizando **Apache JMeter** como herramienta de pruebas.

📎 **Enlace al video:** https://www.youtube.com/watch?v=4oMtdjchvmY

---

## 📌 Descripción del Proyecto

El sistema desarrollado incluye:

- Un **servidor TCP** implementado en Python.
- Manejo de concurrencia mediante **ThreadPoolExecutor**.
- Un mecanismo de **persistencia** para almacenar los resultados de cada petición.
- Pruebas de carga y concurrencia realizadas con **Apache JMeter**.

Cada cliente envía un mensaje al servidor. El servidor procesa la información, genera una respuesta y la devuelve al cliente, registrando además la información relevante en un archivo de log.

---

## 🧠 Arquitectura y Tecnologías

- **Lenguaje:** Python  
- **Comunicación:** TCP (sockets)  
- **Concurrencia:** Thread Pool (`concurrent.futures.ThreadPoolExecutor`)  
- **Sincronización:** `threading.Lock`  
- **Persistencia:** Archivo de texto (logs)  
- **Pruebas de rendimiento:** Apache JMeter  

El uso de un Thread Pool permite:
- Controlar el número máximo de hilos activos
- Evitar la creación excesiva de threads
- Mantener estabilidad bajo múltiples conexiones simultáneas

---

## 📊 Pruebas de Rendimiento con JMeter

Se utilizó **Apache JMeter** para simular múltiples clientes TCP enviando peticiones en paralelo al servidor.  
Las pruebas permitieron analizar:

- Comportamiento del servidor bajo concurrencia
- Tiempo de respuesta
- Manejo de múltiples solicitudes simultáneas
- Impacto del límite de hilos configurado

La configuración incluye:
- **Thread Group**
- **TCP Sampler**
- Uso de **variables** para generar mensajes dinámicos

---

## 💾 Persistencia de Datos

Cada solicitud procesada por el servidor se almacena en un archivo de log, incluyendo:

- Fecha y hora
- Dirección IP del cliente
- Mensaje recibido
- Resultado del procesamiento

Para evitar condiciones de carrera, el acceso al archivo está protegido mediante un **lock**, garantizando escritura segura en entornos concurrentes.

---

## 📄 Documentación

El repositorio incluye un **archivo PDF** donde se explica:

- La implementación del servidor
- El funcionamiento del Thread Pool
- La configuración de JMeter
- Resultados obtenidos
- Conclusiones del proyecto

  
