import {useEffect, useState} from "react";
import {NavLink} from "react-router-dom";
import YandexMap from "../components/YandexMap";
import {Filters} from "../components/Filters";


export const MainPage = () => {
    return(
        <div>
            <Filters/>
            <YandexMap/>
        </div>
    )
}