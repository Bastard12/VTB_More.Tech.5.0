import {
    createBrowserRouter, Link, NavLink, Outlet,
    RouterProvider, useNavigate,
} from "react-router-dom";
import {useEffect, useState} from "react";
import "../styles/main.css"
import {} from "../assets/images/VTB_logo_ru.png"

export const Navbar = () => {

    let [redirectState, setRedirectState] = useState(false);
    const [navabarState, setNavbarState] = useState(false);

    const navigate = useNavigate();

    useEffect(() => {
        setRedirectState(false)
        if (redirectState) {
            navigate('/');
        }
    }, [navigate, redirectState]);

    return(
        <>

            <style>
                @import url('https://fonts.googleapis.com/css2?family=Alegreya+Sans+SC:ital,wght@1,300&family=Montserrat+Alternates:wght@500&family=Mulish:wght@300&display=swap');
            </style>
            <nav className="bg-white shadow shadow-gray-100">
                <div>
                    <div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
                        <NavLink to={"/"}>
                            <img src={require('../assets/images/VTB_logo_ru.png')} alt="logo" className="h-10 w-auto" />
                        </NavLink>
                    </div>
                </div>

            </nav>
        </>
    );
}