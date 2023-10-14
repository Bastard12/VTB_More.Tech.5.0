import {
    createBrowserRouter, Link, NavLink, Outlet,
    RouterProvider, useNavigate,
} from "react-router-dom";
import {useEffect, useState} from "react";

export const YandexMap = () => {
    return(
        <div>
            <head>
                <script src="https://api-maps.yandex.ru/2.1/?apikey=<5941ca0f-88a5-462a-b68b-049e98bd248c>&lang=ru_RU" type="text/javascript">
                </script>
            </head>
            <body>
                <div id="map" className= "w-[1176px] h-[644px]"></div>
                <script src="../scripts/LoadingYandexMap.js" type="text/javascript"></script>
            </body>
        </div>
    );
}