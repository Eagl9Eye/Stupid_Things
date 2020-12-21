#include <ESP8266WiFi.h>
#include <espnow.h>
#define MAX_PEERS (8)
#define MAC_LENGTH (6)

typedef struct {
  uint8_t address[MAC_LENGTH];
} MAC;
typedef struct body {
  int light;
} body;

MAC peers[MAX_PEERS] =
{
    {0xBC, 0xDD, 0xC2, 0x7A, 0xDC, 0xC2},
    {0xBC, 0xDD, 0xC2, 0x7A, 0xD6, 0x7A}
};
body data;

int state, oldstate;
unsigned long timerDelay = 50;  // refreshing rate

String convertMAC(MAC mac_addr[]) {
  for(int i=0;i<MAX_PEERS;i++)
    {
        Serial.print("MAC[");
        Serial.print(i);
        Serial.print("]\t");
        MAC addr = mac_addr[i];
        uint8_t *p = addr.address;
        int j = 0;
        while(*p)
        {
            Serial.print(*p++, HEX);
            if(++j!=MAC_LENGTH)
            {
                Serial.print(":");
            }
        }
        Serial.print("\n");
    }
}

void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Packet send to: [");
  Serial.print(*mac_addr);
  Serial.print("] -> ");
  if (sendStatus == 0){
    Serial.println("success");
  }
  else{
    Serial.println("fail");
  }
  digitalWrite(D4, sendStatus);
}

void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.print("ESP8266 Board MAC Address:  ");
  Serial.println(WiFi.macAddress());
  convertMAC(peers);
  pinMode(D7, INPUT);
  pinMode(D4, OUTPUT);
  WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // Once ESPNow is successfully Init, we will register for Send CB to
  // get the status of Trasnmitted packet
  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(OnDataSent);
  
  // Register peer
  for(int i=0;i<MAX_PEERS;i++)
  {
    MAC addr = peers[i];
    uint8_t *addr_u8 = addr.address; 
    esp_now_add_peer(addr_u8, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
  }
}

void loop() {
  state = digitalRead(D7);
  if(state != oldstate){
    data.light = state;
    // Send message via ESP-NOW
    for(int i=0;i<MAX_PEERS;i++)
    {
      MAC addr = peers[i];
      uint8_t *addr_u8 = addr.address; 
      esp_now_send(addr_u8, (uint8_t *) &data, sizeof(data));
    }
    Serial.print(data.light);
    Serial.println(" send!");
    digitalWrite(D4, 0);
  }
  oldstate = state;
  delay(timerDelay);
}
