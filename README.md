# screenshot_backend
一個簡易的 websocket server，用於將前端的視訊影像截圖並自動傳送至後端，以進行後續處理

## Server side([參考](https://github.com/Pithikos/python-websocket-server))

### 1. installation
install websocket-server
```bash
pip install websocket-server
```

### 2. how to use
1. 設定 server port
```python
PORT = 5000
```

2. function 說明
- **new_client**：client 連接成功後執行
- **client_left**：client 連接中斷時執行
- **message_received**：自 client 接收到訊息時執行，將接收到的圖片寫入 jpg 檔
```python
def message_received(client, server, message):
    ...
    
    # save image sent by the client
    path = ""
    with open(path + "myfile" + uni_name + ".jpg", "wb") as f:
        ...
```
*\*path可自行替換存放圖片之資料夾*

*\*若有需要可自行新增 function*

## [Client side](https://github.com/sean820117/joberfly/blob/websocket/pages/websocket.vue)

### 1. how to use
1. 使用前記得允許使用電腦鏡頭錄影

2. 整體流程：鏡頭進行視訊功能，每 20 毫秒會以 canvas 繪製一張截圖以顯示給前端使用者(canvasDraw)並生成 canvas 文字框，每 20 張 canvas 即傳送一張圖片資料給 Server 進行處理(ImageLimit、sendMessage)

3. 修改參數：
-  websocket設定需與 Server port(5000) 一致
```js
this.ws = new WebSocket('ws://localhost:5000');
```
-  測試時間，超過時間即停止，目前設定 10 秒
```js
let cleartimer = setTimeout(() => {
    clearInterval(this.timer)
}, 10000);
```
-  canvas繪製的間隔時間(顯示給前端使用者看的)，目前設定 20 毫秒
```js
methods:{
    canvasDraw(){
        this.timer = setInterval(() => {
                ...
        }, 20);
    }
}
```
-  limit_num：每間隔 x 張 canvas 即傳送圖片資料至 Server 進行處理，目前設定間隔 20 張(即每 20 張傳送一張)
```js
methods:{
    ImageLimit(image_data){
        let limit_num = 20
        ...
    }
}
```
-  canvas 文字框樣式，可自行調整
```js
methods:{
    drawWordCanvas(){
        ...
        
        // style setting
        cw.width = canvas.width * 0.9
        cw.height = 40
        ctx.fillStyle = 'pink'
        ctx.fillRect(0, 0, cw.width, cw.height);

        ctx.font = "bold 15px arial"
        ctx.textAlign = "center";
        ctx.fillStyle = 'black'

        ...
    },
}
```
-  canvas 文字框文字內容(this.canvasWord)，可自行調整
```js
methods:{
    drawWordCanvas(){
        ...
        
        // style setting
        ...

        ...
        // 讓canvas文字框的文字自動換行
        this.wrapText(this.canvasWord, cw.width/2, 25);
    },
}
```
