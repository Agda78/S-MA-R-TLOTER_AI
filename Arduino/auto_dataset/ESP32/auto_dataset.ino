#include    "esp_camera.h"
#include    "Arduino.h"
#include    "soc/soc.h"           // Disable brownour problems
#include    "soc/rtc_cntl_reg.h"  // Disable brownour problems
#include    "driver/rtc_io.h"
#include    <WiFi.h>

// Pin definition for CAMERA_MODEL_AI_THINKER
#define     PWDN_GPIO_NUM       32
#define     RESET_GPIO_NUM      -1
#define     XCLK_GPIO_NUM       0
#define     SIOD_GPIO_NUM       26
#define     SIOC_GPIO_NUM       27

#define     Y9_GPIO_NUM         35
#define     Y8_GPIO_NUM         34
#define     Y7_GPIO_NUM         39
#define     Y6_GPIO_NUM         36
#define     Y5_GPIO_NUM         21
#define     Y4_GPIO_NUM         19
#define     Y3_GPIO_NUM         18
#define     Y2_GPIO_NUM         5
#define     VSYNC_GPIO_NUM      25
#define     HREF_GPIO_NUM       23
#define     PCLK_GPIO_NUM       22

#define     TEMPOTRAFOTO        5

int pictureNumber;
const char* ssid = "**********";
const char* password = "***********";
const char* host = "192.168.1.21"; 
const int port = 5011;

camera_config_t  camera_cfg();
void camera_init(camera_config_t*);
void connect_to_WiFi();
camera_fb_t * take_a_pic();



void setup() {
    WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0); //disable brownout detector
    Serial.begin(115200);
    camera_config_t camcfg = camera_cfg();
    camera_init(&camcfg);
    connect_to_WiFi();
    int pictureNumber = 0;
}

void loop() {
    WiFiClient esp32cam_client;

    //Il client esp32cam_client prova a connettersi al server python sulla macchina dove verrano conservate le foto

    while (!esp32cam_client.connect(host, port)) {
        Serial.println("Connessione al server fallita");
        delay(1000);
    }
    pictureNumber++;
    camera_fb_t * foto2send = take_a_pic();

    //mandiamo la foto al server python sulla macchina dove verranno conservate le foto
    //manda prima la dimensione della foto
    esp32cam_client.write((const uint8_t*) &foto2send->len, sizeof(foto2send->len));

    //manda il payload effettivo
    esp32cam_client.write(foto2send->buf, foto2send->len);

    esp_camera_fb_return(foto2send); 
    esp32cam_client.stop();
    delay(TEMPOTRAFOTO*1000);
}

camera_config_t camera_cfg(){
    camera_config_t config;
    config.ledc_channel = LEDC_CHANNEL_0;
    config.ledc_timer = LEDC_TIMER_0;
    config.pin_d0 = Y2_GPIO_NUM;
    config.pin_d1 = Y3_GPIO_NUM;
    config.pin_d2 = Y4_GPIO_NUM;
    config.pin_d3 = Y5_GPIO_NUM;
    config.pin_d4 = Y6_GPIO_NUM;
    config.pin_d5 = Y7_GPIO_NUM;
    config.pin_d6 = Y8_GPIO_NUM;
    config.pin_d7 = Y9_GPIO_NUM;
    config.pin_xclk = XCLK_GPIO_NUM;
    config.pin_pclk = PCLK_GPIO_NUM;
    config.pin_vsync = VSYNC_GPIO_NUM;
    config.pin_href = HREF_GPIO_NUM;
    config.pin_sscb_sda = SIOD_GPIO_NUM;
    config.pin_sscb_scl = SIOC_GPIO_NUM;
    config.pin_pwdn = PWDN_GPIO_NUM;
    config.pin_reset = RESET_GPIO_NUM;
    config.xclk_freq_hz = 20000000;
    config.pixel_format = PIXFORMAT_JPEG; 

    if(psramFound()){
    config.frame_size = FRAMESIZE_UXGA; // FRAMESIZE_ + QVGA|CIF|VGA|SVGA|XGA|SXGA|UXGA
    config.jpeg_quality = 10;
    config.fb_count = 2;
    } else {
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 12;
    config.fb_count = 1;
    }
    return config;
}

void camera_init(camera_config_t* cfgptr){
    esp_err_t err = esp_camera_init(cfgptr);
    if (err != ESP_OK) {
        Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }
}

void connect_to_WiFi(){
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
}

camera_fb_t * take_a_pic(){
    camera_fb_t * foto = esp_camera_fb_get();
    if (!foto) {
        Serial.println("Cattura fallita. Il programma termina");
        return NULL;
    }
    else return foto;
}



