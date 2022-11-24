import { NavLink } from "react-router-dom";

export default function Nav() {
    return (
        <div className='max-w-xs'>
            <div className='overflow-y-auto py-4 px-3 bg-gray-50 rounded dark:bg-gray-800'>
                <ul className='space-y-2'>
                    <NavLink to="closets/" className="text-white flex items-center p-2">
                        Dashboard
                    </NavLink>
                    <NavLink to="closets/" className="text-white flex items-center p-2">
                        item 1
                    </NavLink>
                    <NavLink to="closets/" className="text-white flex items-center p-2">
                        item 1
                    </NavLink>
                    <NavLink to="closets/" className="text-white flex items-center p-2">
                        item 1
                    </NavLink>
                    <NavLink to="closets/" className="text-white flex items-center p-2">
                        item 1
                    </NavLink>
                </ul>
            </div>
        </div>
    );
};
