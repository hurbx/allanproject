import {useEffect, useState} from 'react';


const Clients = () => {
    const [clients, setClients] = useState([]);
    useEffect(() => {
    const fetchClients = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/client_list/');
        const data = await response.json();
        setClients(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  }, []);

    console.log(clients);



    return (
        <div>Clientes</div>
    )
}
export default Clients;