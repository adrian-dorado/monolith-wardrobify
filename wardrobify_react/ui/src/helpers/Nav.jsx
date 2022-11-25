import { useState } from "react";
import { NavLink } from "react-router-dom";
import { AiOutlineMenu } from "react-icons/ai";


export default function Nav() {
    const [sidebar, setSidebar] = useState(false)

    const showSidebar = () => setSidebar(!sidebar)

    return (
        <nav className="flex items-center flex-wrap justify-between bg-gray-50 h-12 text-white dark:bg-gray-800">
            <div className="ml-4">
                <AiOutlineMenu onClick={showSidebar}/>
            </div>
            <NavLink to='/'>
                Homepage
            </NavLink>
            <div className="mr-4">
                Log In!
            </div>
        </nav>

    );
};
