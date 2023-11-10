import React from 'react';
import styled from 'styled-components';
import {Button} from 'primereact/button';


const CustomCard = ({ title, imagen, alt, pos }) => {
    return (
        <Wrapper pos={pos}>
            <div className={'container'}>
                <div className={'card'}>
                    <img className={'card-image'} src={imagen} alt={alt} />
                    <div className={'overlay-buttom'}>
                         <Button label={title} outlined size={'small'}/>
                    </div>
                </div>

            </div>
        </Wrapper>
    )
}
export default CustomCard;

const Wrapper = styled.div`
    .container {
      padding: 1rem;
      perspective: 60rem;
      width: 200px;
      height: 300px;
      background-color: transparent;
    }
    .card {
      width: 200px;
      aspect-ratio: 4/3;
      transition: rotate 500ms ease, scale 700ms ease;
      background-color: transparent;
      height: 300px;
      
    }
  .card-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 1rem;
    box-shadow: -4px 37px 29px -26px rgba(59,55,55,0.56);
-webkit-box-shadow: -4px 37px 29px -26px rgba(59,55,55,0.56);
-moz-box-shadow: -4px 37px 29px -26px rgba(59,55,55,0.56);
  }
  
  .container:hover .card {
  transform: ${({ pos }) => {
    if (pos === 'left') {
      return 'rotateY(20deg) scale(1.1)';
    }
    if (pos === 'right') {
      return 'rotateY(-20deg) scale(1.1)';
    } else {
      return 'rotateX(0deg) scale(1.02)';
    }
  }};
}
  .overlay-buttom {
    position: absolute;
    top: 50%;
    left: 10%;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

  }
  
`