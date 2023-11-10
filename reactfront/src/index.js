import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import 'primeicons/primeicons.css';
import reportWebVitals from './reportWebVitals';
import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
import "primereact/resources/themes/lara-dark-teal/theme.css";
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <PrimeReactProvider>
    <App />
  </PrimeReactProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
