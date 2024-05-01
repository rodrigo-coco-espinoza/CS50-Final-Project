import { Link } from 'react-router-dom'
import { TypeAnimation } from 'react-type-animation'

function Buscador(){

    return (

        <section className='flex md:flex-row flex-col-reverse sm:py-16 py-6 cursor-default'>
        
            {/* Contenido lado izquierdo */}
            <div className='flex-1 flex flex justify-center items-center md:mr-10 mr-0 md:mt-0 mt-10 relative'>
                <TypeAnimation
                    style={{ 
                        whiteSpace: 'pre-line', 
                        height: '280px', 
                        display: 'block',
                        fontSize: '1.5em'
                        }}
                    sequence={[
                        `PC Isla Administrator\n \u00A0 \u00A0 \u00A0 Responsive web app,
                        \u00A0 \u00A0 \u00A0 Register projects,
                        \u00A0 \u00A0 \u00A0 Manage accounts,
                        \u00A0 \u00A0 \u00A0 Monitor attedance,
                        \u00A0 \u00A0 \u00A0 File storage.`,
                        1000,
                        '',
                    ]}
                    repeat={Infinity}
                />
            </div>
            {/* Contenido lado derecho */}
            <div className='flex-1  justify-center items-start flex-col'>
                <h2 className='font-semibold xs:text-[48px] text-azul-brillante-400 text-[44px] xs:leading-[76.8px] leading-[66.8px] w-full'>Project description</h2>
                <p className='text-azul-marino-300 text-[18px] leading-[30.8px] mt-5 max-w-[470px] mb-5'>At my job in tax administration, we have a large amount of data that is of interest to various state institutions, which seek to obtain statistical data about the country's taxpayers. This is why we have made available 3 computers called PC Isla (island), so that institutions can request the use of these computers for 3-month projects. Our task is to register and manage the projects, as well as monitor their attendance.</p>
            </div>
        </section>



    )
}


export default Buscador
