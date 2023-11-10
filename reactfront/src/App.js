import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Nav from './components/Nav';
import Clients from './components/Clients';
import Proveedores from './components/Proveedores';
import Itinerario from './components/Itinerario';
import Init from "./components/Init";

const App = () => {
  return (
    <Router>
      <Nav />
      <Routes>
        <Route path="/" element={<Init />} />
        <Route path="/clients" element={<Clients />} />
        <Route path="/proveedores" element={<Proveedores />} />
        <Route path="/itinerario" element={<Itinerario />} />
      </Routes>
    </Router>
  );
};

export default App;

