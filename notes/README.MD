- Serializer: digunakan utk memformat data ke bentuk json
- Websocket : digunakan utk realtime data processing

- Step by step frontend:
    - install create-react-app (npm install -g create-react-app)
    - npm global disimpan di C:\Users\[nama_user]\AppData\Roaming\npm\node_modules\
    - buat react app frontend (create-react-app frontend)
    - masuk ke folder frontend (cd frontend)
    - jalankan frontend server (npm start)
    - install reactstrap (npm install --save reactstrap)
    - install bootstrap (npm install bootstrap -S)
    
- Step by step react:
    - pindahkan semua file css dari app.js ke index.js
    - membuat container di App.js: 
        - import React, {Component} from 'react';
        - import {Button, Container, Row, Col} from 'reactstrap';
    - membuat component:
        - buat folder components
        - buat component disimpan dengan file .js
     