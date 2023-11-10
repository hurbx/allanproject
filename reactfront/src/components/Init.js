import CustomCard from "./CustomCard";
import React from "react";
import { useNavigate } from "react-router-dom";

const Init = () => {
    const navigate = useNavigate()
     const handleCardClick = (route) => {navigate(route)}
    
    return (
        <div style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            minHeight: '100vh',
            gap: 60,
        }}>
            <div onClick={() => handleCardClick('/itinerario')}>
                <CustomCard
                    pos={'left'}
                    title={'Itinerario'}
                    alt={'viaje'}
                    imagen={'https://conservationreserves.org/wp-content/uploads/2021/06/EXP1741-scaled-e1627922461189.jpg'}
                />
            </div>

            <div onClick={() => handleCardClick('/proveedores')}>
                <CustomCard
                    pos={'center'}
                    title={'Proveedores'}
                    alt={'proveedores'}
                    imagen={'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-dBuZSOcxelVbzmfVFMv6XEezmhk90ph2kg&usqp=CAU'}
                />
            </div>

            <div onClick={() => handleCardClick('/clients')}>
                <CustomCard
                    pos={'right'}
                    title={'Clientes'}
                    alt={'proveedores'}
                    imagen={'https://images.inc.com/uploaded_files/image/1920x1080/getty_678074927_2000133320009280137_360656.jpg'}
                />
            </div>
        </div>

    )
}
export default Init;