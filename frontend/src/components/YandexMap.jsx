import {
    createBrowserRouter, Link, NavLink, Outlet,
    RouterProvider, useNavigate,
} from "react-router-dom";
import {useEffect, useState} from "react";

export const YandexMap = () => {
    ymaps.ready(function () {
        var myMap = new ymaps.Map('map', {
            center: [55.751574, 37.573856],
            zoom: 9,
            // Также доступны наборы 'default' и 'largeMapDefaultSet'
            // Элементы управления в наборах подобраны оптимальным образом
            // для карт маленького, среднего и крупного размеров.
            controls: ['smallMapDefaultSet']
        }, {
            searchControlProvider: 'yandex#search'
        });
    });
    return(
        <div>
            <head>
                <script src="https://api-maps.yandex.ru/2.1/?apikey=5941ca0f-88a5-462a-b68b-049e98bd248c&lang=ru_RU" type="text/javascript">
                </script>
            </head>
            <body>
                <div id="map" style="width: 1176px; height: 644px"></div>
            </body>
        </div>
    );
}