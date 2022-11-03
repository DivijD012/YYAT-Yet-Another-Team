#include <WiFi.h>
#include <WebServer.h>
#include <WiFiClient.h>
#include <HTTPClient.h>
#include <ThingSpeak.h>

//char* ssid = "vnnm_realme";
//char* password = "00000000";
//char ssid[] = "Galaxy M3125C5";
//char password[] = "udge3324";
char ssid[] = "esw-m19@iiith";
char password[] = "e5W-eMai@3!20hOct";

#include <Wire.h>
#include <Adafruit_AMG88xx.h>

Adafruit_AMG88xx amg;

long channelID = 1904936;

const char* api_key = "DVRJLFB9UVV22N9P";

float pixels[AMG88xx_PIXEL_ARRAY_SIZE];

int PIR_output = 33;

WebServer server(80);

String data = "";

void fun()
{
  int min_temp = 100;
  int max_temp = -1;
    data = "";
        amg.readPixels(pixels);
    data += "[";
    for(int i=1; i<=AMG88xx_PIXEL_ARRAY_SIZE; i++){
      if(min_temp > pixels[i-1]) { min_temp = pixels[i-1];}
      if(max_temp < pixels[i-1]) { max_temp = pixels[i-1];}
      String input_data = String(pixels[i-1]);
      data += input_data;
      if( i != AMG88xx_PIXEL_ARRAY_SIZE){ Serial.print(","); data += ",";}
    }
    data += "]";
    data += "\n";
    String uwu = "uwu";
//    ThingSpeak.writeField(channelID, 1,uwu,api_key);
    ThingSpeak.writeField(channelID, 3,min_temp,api_key);
    delay(30000);
    ThingSpeak.writeField(channelID, 4,max_temp,api_key);
    delay(30000);
  server.send(200,"text/html",data);
  Serial.println("Sent!");
}

void index1()
{
    String s = "<html>";
     s +="   <head>";
     s +="     <script src=\"https://cdn.jsdelivr.net/npm/p5@1.4.2/lib/p5.js\"></script>";
     s +="     <script src=\"sketch.js\"></script>";
     s +="   </head>";
     s +="   <body>";
     s +="     <main>";
     s +="     </main>";
     s +="   </body>";
     s +=" </html>";

 server.send(200,"text/html",s);
}

void js()
{
String s = "const max_temp = 30\n"; 
 s += "const min_temp = 20\n"; 
 s += "\n"; 
 s += "const camColors = [0x480F,\n"; 
 s += "    0x400F,0x400F,0x400F,0x4010,0x3810,0x3810,0x3810,0x3810,0x3010,0x3010,\n"; 
 s += "    0x3010,0x2810,0x2810,0x2810,0x2810,0x2010,0x2010,0x2010,0x1810,0x1810,\n"; 
 s += "    0x1811,0x1811,0x1011,0x1011,0x1011,0x0811,0x0811,0x0811,0x0011,0x0011,\n"; 
 s += "    0x0011,0x0011,0x0011,0x0031,0x0031,0x0051,0x0072,0x0072,0x0092,0x00B2,\n"; 
 s += "    0x00B2,0x00D2,0x00F2,0x00F2,0x0112,0x0132,0x0152,0x0152,0x0172,0x0192,\n"; 
 s += "    0x0192,0x01B2,0x01D2,0x01F3,0x01F3,0x0213,0x0233,0x0253,0x0253,0x0273,\n"; 
 s += "    0x0293,0x02B3,0x02D3,0x02D3,0x02F3,0x0313,0x0333,0x0333,0x0353,0x0373,\n"; 
 s += "    0x0394,0x03B4,0x03D4,0x03D4,0x03F4,0x0414,0x0434,0x0454,0x0474,0x0474,\n"; 
 s += "    0x0494,0x04B4,0x04D4,0x04F4,0x0514,0x0534,0x0534,0x0554,0x0554,0x0574,\n"; 
 s += "    0x0574,0x0573,0x0573,0x0573,0x0572,0x0572,0x0572,0x0571,0x0591,0x0591,\n"; 
 s += "    0x0590,0x0590,0x058F,0x058F,0x058F,0x058E,0x05AE,0x05AE,0x05AD,0x05AD,\n"; 
 s += "    0x05AD,0x05AC,0x05AC,0x05AB,0x05CB,0x05CB,0x05CA,0x05CA,0x05CA,0x05C9,\n"; 
 s += "    0x05C9,0x05C8,0x05E8,0x05E8,0x05E7,0x05E7,0x05E6,0x05E6,0x05E6,0x05E5,\n"; 
 s += "    0x05E5,0x0604,0x0604,0x0604,0x0603,0x0603,0x0602,0x0602,0x0601,0x0621,\n"; 
 s += "    0x0621,0x0620,0x0620,0x0620,0x0620,0x0E20,0x0E20,0x0E40,0x1640,0x1640,\n"; 
 s += "    0x1E40,0x1E40,0x2640,0x2640,0x2E40,0x2E60,0x3660,0x3660,0x3E60,0x3E60,\n"; 
 s += "    0x3E60,0x4660,0x4660,0x4E60,0x4E80,0x5680,0x5680,0x5E80,0x5E80,0x6680,\n"; 
 s += "    0x6680,0x6E80,0x6EA0,0x76A0,0x76A0,0x7EA0,0x7EA0,0x86A0,0x86A0,0x8EA0,\n"; 
 s += "    0x8EC0,0x96C0,0x96C0,0x9EC0,0x9EC0,0xA6C0,0xAEC0,0xAEC0,0xB6E0,0xB6E0,\n"; 
 s += "    0xBEE0,0xBEE0,0xC6E0,0xC6E0,0xCEE0,0xCEE0,0xD6E0,0xD700,0xDF00,0xDEE0,\n"; 
 s += "    0xDEC0,0xDEA0,0xDE80,0xDE80,0xE660,0xE640,0xE620,0xE600,0xE5E0,0xE5C0,\n"; 
 s += "    0xE5A0,0xE580,0xE560,0xE540,0xE520,0xE500,0xE4E0,0xE4C0,0xE4A0,0xE480,\n"; 
 s += "    0xE460,0xEC40,0xEC20,0xEC00,0xEBE0,0xEBC0,0xEBA0,0xEB80,0xEB60,0xEB40,\n"; 
 s += "    0xEB20,0xEB00,0xEAE0,0xEAC0,0xEAA0,0xEA80,0xEA60,0xEA40,0xF220,0xF200,\n"; 
 s += "    0xF1E0,0xF1C0,0xF1A0,0xF180,0xF160,0xF140,0xF100,0xF0E0,0xF0C0,0xF0A0,\n"; 
 s += "    0xF080,0xF060,0xF040,0xF020,0xF800];\n"; 
 s += "    \n"; 
 s += "    var k = 5\n"; 
 s += "    \n"; 
 s += "    \n"; 
 s += "    \n"; 
 s += "    function setup() {\n"; 
 s += "      createCanvas(400, 400);\n"; 
 s += "      frameRate(3);\n"; 
 s += "    }\n"; 
 s += "    \n"; 
 s += "    function constain(x, l, r){\n"; 
 s += "        if(x < l)\n"; 
 s += "            return l;\n"; 
 s += "        if(x > r)\n"; 
 s += "            return r;\n"; 
 s += "        return x;\n"; 
 s += "    }\n"; 
 s += "    \n"; 
 s += "    function mip(x, a1, b1, a2, b2){\n"; 
 s += "      let ratio = (x-a1)/(b1-a1);\n"; 
 s += "      return Math.floor(ratio*(b2-a2) + a2);\n"; 
 s += "    }\n"; 
 s += "    function httpGt(theUrl)\n"; 
 s += "    {\n"; 
 s += "        var xmlHttp = new XMLHttpRequest();\n"; 
 s += "        xmlHttp.open( \"GET\", theUrl, false ); // false for synchronous request\n"; 
 s += "        xmlHttp.send( null );\n"; 
 s += "        console.log(xmlHttp.responseText);\n"; 
 s += "        return xmlHttp.responseText;\n"; 
 s += "        \n"; 
 s += "    }\n"; 
 s += "    function draw() {\n"; 
 s += "      let p = JSON.parse(\"{ \\\"value\\\" : \" + httpGt('http://192.168.43.181/') + \" }\" );\n"; 
 s += "      let dat = p[\"value\"] ;\n"; 
 s += "      background(220);\n"; 
 s += "      noStroke();\n"; 
 s += "      var side = 50;\n"; 
 s += "      for(var i = 0; i < 8; i++)\n"; 
 s += "        for(var j = 0; j < 8; j++){\n"; 
 s += "          let ind = mip(dat[i*8 + j], 21, 32, 0, 255);\n"; 
 s += "           ind = constain(ind, 0, 255);\n"; 
 s += "          let hexValue = camColors[ind];\n"; 
 s += "          let r = ((hexValue >> 11) & 0x1F);  // Extract the 5 R bits\n"; 
 s += "          let g = ((hexValue >> 5) & 0x3F);   // Extract the 6 G bits\n"; 
 s += "          let b = ((hexValue) & 0x1F);     // Extract the 5 B bits\n"; 
 s += "          // console.log(ind); \n"; 
 s += "          let c = color(ind, 52, 52);\n"; 
 s += "          fill(c);\n"; 
 s += "          // console.log(i);\n"; 
 s += "          square(i*side, j*side, side);\n"; 
 s += "        }\n"; 
 s += "        k++;\n"; 
 s += "        // k = Math.min(12, k);\n"; 
 s += "    }";
 
 server.send(200,"text/html",s);
}

void pirf()
{
   int val = digitalRead(PIR_output);
   if( val == HIGH) 
   {
    server.send(200,"text/html","PIR HIGH");
   }
   if( val == LOW) 
   {
    server.send(200,"text/html","PIR LOW");
   }

   ThingSpeak.writeField(channelID, 2,val,api_key);
}


WiFiClient client;

void setup() {
//  pinMode(sensor,INPUT);
  Serial.begin(9600);
 
  WiFi.begin(ssid,password);
  Serial.print("Connecting to: ");
  Serial.print(ssid);
  Serial.println("...");

  while(WiFi.status()!=WL_CONNECTED)
   {
      delay(1000);
      Serial.print("Connect");
   }

   Serial.print("IP address: ");
   Serial.println(WiFi.localIP());

   server.on("/",fun);
   server.on("/index",index1);
   server.on("/sketch.js",js);
   server.on("/pir",pirf);
   server.begin();

    Serial.println(F("AMG88xx pixels"));

    bool status;
    
    // default settings
    status = amg.begin();
    if (!status) {
        Serial.println("Could not find a valid AMG88xx sensor, check wiring!");
//        while (1);
    }
    
    Serial.println("-- Pixels Test --");

    Serial.println();

    ThingSpeak.begin(client);

    pinMode(PIR_output, INPUT);

    delay(100); // let sensor boot up
}


void loop() {
  // put your main code here, to run repeatedly:
  server.handleClient();
    //read all the pixels

    


    //delay a second
    delay(100);
}
