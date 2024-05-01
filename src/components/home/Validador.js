import { Link } from 'react-router-dom'
import data_validation from 'assets/img/data_validation.png'

function Validador(){

    return (
        <section className='flex md:flex-row flex-col py-8 cursor-default'>
            {/* Contenido lado izquierdo */}
            <div className='flex-col flex-1 flex justify-center items-center md:ml-10 ml-0 md:mt-0 mt-10 relative`'>
            <img src={data_validation} alt="Imagen validación de datos" className='realtive z-[5] sm-sii:-ml-8 max-h-[400px]' />
            </div>
            {/* Contenido lado derecho */}
            
            <div className='flex-1 flex-col flex justify-center items-start '>
                <h2 className='font-semibold xs:text-[48px] text-azul-brillante-400 text-[44px] xs:leading-[76.8px] leading-[66.8px] w-full'>App Details</h2>
                <p className='text-azul-marino-300 text-[18px] leading-[30.8px] mt-5 max-w-[470px]'>This application was developed using Django, React, and Tailwind CSS. Although we learned Flask, Jinja, and Bootstrap in CS50, I found it to be a good challenge to learn another stack and have more tools for the future.
                <br/><br/>
                The database is preloaded with accounts and projects to make the demonstration easier (see README). 
                </p>
               
            </div>
        </section>


    )
}


export default Validador
