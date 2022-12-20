import { useState } from "react";
import { NavLink } from "react-router-dom";
import Dropdown from "./Dropdown"
import { AiOutlineMenu } from "react-icons/ai";


export default function Nav() {
    const [sidebar, setSidebar] = useState(false)

    const showSidebar = () => setSidebar(!sidebar)

    return (
        <>
            <div className="flex items-center flex-wrap justify-between bg-gray-50 h-12 text-white bg-blue-transparent">
                <button className='bg-slate-400 rounded'>
                    <div className="ml-4">
                        <AiOutlineMenu onClick={showSidebar} />
                    </div>
                </button>
                <NavLink to='/'>
                    Homepage
                </NavLink>
                <button className="bg-pink-100">
                    <div className="mr-4 text-green-500">
                        Log In!
                    </div>
                </button>
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
                        <Dropdown />
                    </div>
                </div>
            </nav>
            {/* End Sidebar */}
        </>
    );
};
