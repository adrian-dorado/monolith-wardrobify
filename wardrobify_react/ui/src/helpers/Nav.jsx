import { useState } from "react";
import { NavLink } from "react-router-dom";
import { AiOutlineMenu } from "react-icons/ai";


export default function Nav() {
    const [sidebar, setSidebar] = useState(false)

    const showSidebar = () => setSidebar(!sidebar)

    return (
        <>
            <div className="flex items-center flex-wrap justify-between bg-gray-50 h-12 text-white dark:bg-gray-800">
                <div className="ml-4">
                    <AiOutlineMenu onClick={showSidebar} />
                </div>
                <NavLink to='/'>
                    Homepage
                </NavLink>
                <div className="mr-4">
                    Log In!
                </div>
            </div>
            {/* Sidebar */}
            <nav className={
                `top-0 inset-y-0 left-0 sm:w-[24vw] md:w-[15vw] 
                  dark:bg-gray-800 p-10 
                    text-white 
                    fixed h-full z-40 
                    ease-in-out duration-500 
                    ${sidebar ? 'translate-y-0' : "translate-y-full"}`}>
                <div className='flex flex-col space-y-1'>
                    <div className="mb-5">
                        <button onClick={showSidebar}>
                            X
                        </button>
                    </div>
                    <div>
                        <NavLink to='/' onClick={showSidebar} className="text-white">
                            Dashboard
                        </NavLink>
                    </div>
                    <div>
                        <NavLink onClick={showSidebar} to='outfits/'>
                            Outfits
                        </NavLink>
                    </div>
                    <div>
                        <NavLink onClick={showSidebar} to='closets/'>
                            Closets
                        </NavLink>
                    </div>
                </div>
            </nav>
            {/* End Sidebar */}
        </>
    );
};
