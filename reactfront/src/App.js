import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Init from "./components/Init";
import Clients from "./components/Clients";
import Proveedores from "./components/Proveedores";
import Itinerario from "./components/Itinerario";

const App = () => {
    return (
      <Router>
          <Routes>
              <Route exact path="/" element={<Init />} />
              <Route exact path="/clients" element={<Clients />} />
              <Route exact path="/proveedores" element={<Proveedores />} />
              <Route exact path="/itinerario" element={<Itinerario/>} />
          </Routes>
      </Router>

    );
}
export default App;
