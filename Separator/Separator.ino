#include <ESP32Servo.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <WiFiClientSecure.h>
#include <NewPing.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#define VALOR_MINIMO 20
#define VALOR_MEDIO 14
#define VALOR_MAXIMO 7

const char* ssid = "**********";
const char* password = "*******";

const char* mqtt_server = "***************************";
const int mqtt_port = 8883;
const char* mqtt_username = "*******";
const char* mqtt_password = "********";

// Definición de los canales a utilizar
const char* CONTROL_STATE_TOPIC = "control-estado";
const char* VALOR_ANALOGICO_TOPIC = "valor-sensor";

const int physicalPin = 23;
const int pinServo=2;
const int ledPin = 22;
const int triggerPin = 12;    // Pin de Trigger del sensor ultrasónico
const int echoPin = 13;       // Pin de Echo del sensor ultrasónico
const int maxDistance = 200;  // Distancia máxima en centímetros

NewPing sonar(triggerPin, echoPin, maxDistance);  // Configura el sensor ultrasónico
Servo servo;

static const char* root_ca PROGMEM = R"EOF( 
-----BEGIN CERTIFICATE-----
MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw
TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
cmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwHhcNMTUwNjA0MTEwNDM4
WhcNMzUwNjA0MTEwNDM4WjBPMQswCQYDVQQGEwJVUzEpMCcGA1UEChMgSW50ZXJu
ZXQgU2VjdXJpdHkgUmVzZWFyY2ggR3JvdXAxFTATBgNVBAMTDElTUkcgUm9vdCBY
MTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAK3oJHP0FDfzm54rVygc
h77ct984kIxuPOZXoHj3dcKi/vVqbvYATyjb3miGbESTtrFj/RQSa78f0uoxmyF+
0TM8ukj13Xnfs7j/EvEhmkvBioZxaUpmZmyPfjxwv60pIgbz5MDmgK7iS4+3mX6U
A5/TR5d8mUgjU+g4rk8Kb4Mu0UlXjIB0ttov0DiNewNwIRt18jA8+o+u3dpjq+sW
T8KOEUt+zwvo/7V3LvSye0rgTBIlDHCNAymg4VMk7BPZ7hm/ELNKjD+Jo2FR3qyH
B5T0Y3HsLuJvW5iB4YlcNHlsdu87kGJ55tukmi8mxdAQ4Q7e2RCOFvu396j3x+UC
B5iPNgiV5+I3lg02dZ77DnKxHZu8A/lJBdiB3QW0KtZB6awBdpUKD9jf1b0SHzUv
KBds0pjBqAlkd25HN7rOrFleaJ1/ctaJxQZBKT5ZPt0m9STJEadao0xAH0ahmbWn
OlFuhjuefXKnEgV4We0+UXgVCwOPjdAvBbI+e0ocS3MFEvzG6uBQE3xDk3SzynTn
jh8BCNAw1FtxNrQHusEwMFxIt4I7mKZ9YIqioymCzLq9gwQbooMDQaHWBfEbwrbw
qHyGO0aoSCqI3Haadr8faqU9GY/rOPNk3sgrDQoo//fb4hVC1CLQJ13hef4Y53CI
rU7m2Ys6xt0nUW7/vGT1M0NPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNV
HRMBAf8EBTADAQH/MB0GA1UdDgQWBBR5tFnme7bl5AFzgAiIyBpY9umbbjANBgkq
hkiG9w0BAQsFAAOCAgEAVR9YqbyyqFDQDLHYGmkgJykIrGF1XIpu+ILlaS/V9lZL
ubhzEFnTIZd+50xx+7LSYK05qAvqFyFWhfFQDlnrzuBZ6brJFe+GnY+EgPbk6ZGQ
3BebYhtF8GaV0nxvwuo77x/Py9auJ/GpsMiu/X1+mvoiBOv/2X/qkSsisRcOj/KK
NFtY2PwByVS5uCbMiogziUwthDyC3+6WVwW6LLv3xLfHTjuCvjHIInNzktHCgKQ5
ORAzI4JMPJ+GslWYHb4phowim57iaztXOoJwTdwJx4nLCgdNbOhdjsnvzqvHu7Ur
TkXWStAmzOVyyghqpZXjFaH3pO3JLF+l+/+sKAIuvtd7u+Nxe5AW0wdeRlN8NwdC
jNPElpzVmbUq4JUagEiuTDkHzsxHpFKVK7q4+63SM1N95R1NbdWhscdCb+ZAJzVc
oyi3B43njTOQ5yOf+1CceWxG1bQVs5ZufpsMljq4Ui0/1lvh+wjChP4kqKOJ2qxq
4RgqsahDYVvTH9w7jXbyLeiNdd8XM2w9U/t7y0Ff/9yi0GE44Za4rF2LN9d11TPA
mRGunUHBcnWEvgJBQl9nJEiU0Zsnvgc/ubhPgXRR4Xq37Z0j4r7g1SgEEzwxA57d
emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=
-----END CERTIFICATE-----
)EOF";

WiFiClientSecure espClient;
PubSubClient client(espClient);

bool enableSensorReading = false;  // Variable de control para habilitar mediciones

void setup_wifi() {
  // Configura la conexión WiFi
  delay(10);
  Serial.println();
  Serial.print("Conectando ");
  for (int y = 0; y < 3; y++) {
    for (int x = 0; x < 1; x++) {
      digitalWrite(ledPin, 0);
      delay(100);
    }
    for (int x = 0; x < 1; x++) {
      digitalWrite(ledPin, 1);
      delay(100);
    }
  }
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi conectado");
  Serial.println("Dirección IP: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Mensaje recibido en el topico: ");
  Serial.println(topic);

  if (strcmp(topic, CONTROL_STATE_TOPIC) == 0) {
    int estado = payload[0] - '0';

    if (estado == 0) {
      digitalWrite(physicalPin, estado);
      digitalWrite(ledPin, estado);
      Serial.print("LED state: ");
      servo.write(0);
      Serial.println(estado);
    } else if (estado == 1) {
      digitalWrite(physicalPin, estado);
      digitalWrite(ledPin, estado);
      servo.write(180);
      Serial.print("LED state: ");
      Serial.println(estado);
    } else if (estado == 2) {
      // Habilita las mediciones cuando se recibe un mensaje en VALOR_ANALOGICO_TOPIC con valor 2
      enableSensorReading = true;
    } else {
      // Deshabilita las mediciones para otros valores
      enableSensorReading = false;
    }
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Conectando a MQTT... ");
    if (client.connect("ESP32Client", mqtt_username, mqtt_password)) {
      Serial.println("Conectado");
      for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 1; x++) {
          digitalWrite(ledPin, 0);
          delay(100);
        }
        for (int x = 0; x < 1; x++) {
          digitalWrite(ledPin, 1);
          delay(100);
        }
      }
      digitalWrite(ledPin, 1);
      delay(500);
      digitalWrite(ledPin, 0);
      client.subscribe(CONTROL_STATE_TOPIC);
      client.subscribe(VALOR_ANALOGICO_TOPIC);
    } else {
      Serial.print("Falla, rc=");
      Serial.print(client.state());
      Serial.println(" Reintentando en 5 segundos");
      delay(5000);
    }
  }
}

void sensorTask(void* parameter) {
  while (1) {
    // Realiza el promedio de 5 lecturas ultrasónicas para
    long totalDist = 0;
    int validReadings = 0;
    for (int i = 0; i < 5; i++) {
      unsigned int distancia = sonar.ping_cm();
      if (distancia > 0 && distancia <= maxDistance) {
        totalDist += distancia;
        validReadings++;
      }
      delay(10);  // Pequeña pausa entre lecturas
    }
    if (validReadings > 0) {
      // Calcula el promedio de las lecturas válidas
      unsigned int promedioDist = totalDist / validReadings;
      String mensaje = String(promedioDist);
      Serial.println(mensaje);
      client.publish(VALOR_ANALOGICO_TOPIC, mensaje.c_str());

      if (promedioDist >= VALOR_MINIMO) {
        servo.write(0);
        digitalWrite(physicalPin, 0);
      }
    }
    // Espera 1 segundo antes de la siguiente medición
    vTaskDelay(1000 / portTICK_PERIOD_MS);  // Pausa de 1
  }
}


void setup() {
  pinMode(physicalPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  servo.attach(pinServo);
  digitalWrite(ledPin, 0);
  Serial.begin(9600);
  servo.write(90);
  setup_wifi();
  espClient.setCACert(root_ca);
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);

  // Tarea del sensor
  xTaskCreatePinnedToCore(
    sensorTask,    // Función de la tarea
    "SensorTask",  // Nombre de la tarea
    10000,         // Tamaño de la pila (en bytes)
    NULL,          // Parámetros de la tarea
    1,             // Prioridad de la tarea
    NULL,          // Manejador de la tarea
    0);            // Núcleo en el que se ejecutará la tarea (El ESP32 solo tiene 2 nucleos)
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
