import React from 'react'
import ReactDOM from 'react-dom' // Corrected this line
import App from './App.jsx'
import './index.css'

import "@fontsource/outfit"

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)